import React, { Component } from "react";
import Card from "./Card";
import CardModal from "./CardModal";
import {
  getApplications,
  updateApplication,
  createApplication,
  deleteApplication,
} from "../api/applicationHandler";

export default class CardBoard extends Component {
  constructor(props) {
    super(props);

    this.state = {
      applications: [],
      card_titles: [],
      card_class: [],
      showModal: false,
    };
    this.groupApplication = this.groupApplication.bind(this);
    this.createCardTitle = this.createCardTitle.bind(this);
    this.createCardClass = this.createCardClass.bind(this);
  }

  async componentDidMount() {
    const res = await getApplications();
    const result = this.groupApplication(res.data);
    const cardTitles = this.createCardTitle(result);
    const cardClass = this.createCardClass(result);
    this.setState({
      applications: res,
      card_titles: cardTitles,
      card_class: cardClass,
    });
    console.log(res);
    console.log(this.state);
  }

  renderPage(newApplications) {
    // helper function to render the page
    // rerender the page to represent the update result
    const result = this.groupApplication(newApplications);
    const cardTitle = this.createCardTitle(result);
    const cardClass = this.createCardClass(result);

    this.setState({
      applications: newApplications,
      card_titles: cardTitle,
      card_class: cardClass,
      showModal: false,
    });
  }

  // the update function for child component
  async updateCardBoard(application) {
    const newApplications = this.state.applications;
    if (!application.id) {
      const res = await createApplication(application);
      newApplications.push(res);
    } else {
      console.log("updating id=" + application.id);
      const res = await updateApplication(application.id, application);
      const updatedApp = res;
      const idx = newApplications.findIndex((a) => a.id === updatedApp.id);
      newApplications[idx] = updatedApp;
    }
    this.renderPage(newApplications);
  }

  async deleteApplication(application) {
    const newApplications = this.state.applications;
    console.log("deleting id=" + application.id);
    const res = await deleteApplication(application.id, application);
    const deletedApp = res.data;
    const idx = newApplications.findIndex((a) => a.id === deletedApp.id);
    newApplications.splice(idx, 1);
    this.renderPage(newApplications);
  }

  // open the card modal according to the application in parameter
  showEditModal(application, mode) {
    const modalMode = mode;

    this.setState({
      showModal: true,
      application: application,
      modalMode: modalMode,
    });
  }

  closeEditModal() {
    this.setState({
      showModal: false,
      application: null,
    });
  }

  // create all cards(application) and make cards having the same class in the same column
  createCardClass(applicationsGroup) {
    return applicationsGroup.reduce((pv, v) => {
      const appClass = (
        <div className="col" key={v.title + "_class"} id={v.title + "_class"}>
          {v.applications.reduce((pv, v) => {
            const card = (
              <Card
                application={v}
                key={v.id}
                showEditModal={this.showEditModal.bind(this, v, "update")}
              />
            );
            pv.push(card);
            return pv;
          }, [])}
          {/* add function not implement */}
          <div className="card card-col">
            <div
              className="card-body new-col"
              onClick={this.showEditModal.bind(
                this,
                { class: v.class },
                "create",
              )}
            >
              <i className="fas fa-plus text-center" />
            </div>
          </div>
        </div>
      );
      pv.push(appClass);
      return pv;
    }, []);
  }

  // create the class title
  createCardTitle(applicationsGroup) {
    return applicationsGroup.reduce((pv, v) => {
      const title = (
        <div className="col" key={v.title + "_title"}>
          <div className="card card-col">
            <div className="card-body noPadding">
              <div
                type="text"
                className="text-center title-col form-control-lg"
              >
                {v.title}
              </div>
            </div>
          </div>
        </div>
      );
      pv.push(title);
      return pv;
    }, []);
  }

  // initialize the data, classify data according to their class
  groupApplication(applications) {
    const result = [
      {
        title: "Wish list",
        applications: [],
        class: "1",
      },
      {
        title: "Waiting for referral",
        applications: [],
        class: "2",
      },
      {
        title: "Applied",
        applications: [],
        class: "3",
      },
      {
        title: "Rejected",
        applications: [],
        class: "4",
      },
    ];
    this.state.applications.forEach((app) => {
      const appClass = result.find((v) => {
        return v.class === app.status;
      });
      appClass.applications.push(app);
    });
    return result;
  }

  render() {
    let applicationModal = null;
    if (this.state.application) {
      applicationModal = (
        <CardModal
          show={this.state.showModal}
          submitFunc={this.updateCardBoard.bind(this)}
          mode={this.state.modalMode}
          application={this.state.application}
          closeEditModal={this.closeEditModal.bind(this)}
          deleteApplication={this.deleteApplication.bind(this)}
        />
      );
    }
    return (
      <span id="tab">
        <div className="row">{this.state.card_titles}</div>
        <div className="row">{this.state.card_class}</div>
        {applicationModal}
      </span>
    );
  }
}
