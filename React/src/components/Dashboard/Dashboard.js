/*!

=========================================================
* Paper Dashboard React - v1.3.0
=========================================================

* Product Page: https://www.creative-tim.com/product/paper-dashboard-react
* Copyright 2021 Creative Tim (https://www.creative-tim.com)

* Licensed under MIT (https://github.com/creativetimofficial/paper-dashboard-react/blob/main/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React from "react";
// react plugin used to create charts
import { Line, Pie } from "react-chartjs-2";
// reactstrap components
import {
  Card,
  CardHeader,
  CardBody,
  CardFooter,
  CardTitle,
  Row,
  Col,
} from "reactstrap";
// core components
import {
  dashboard24HoursPerformanceChart,
  dashboardEmailStatisticsChart,
  dashboardNASDAQChart,
} from "variables/charts.js";

function Dashboard() {
  return (
    <>
      
      <div class="content">
        <div class="row">
          <div class="ml-auto mr-auto col-md-8">
            <div class="card-user card">
              <div class="card-header">
                <h5 class="card-title">Choose Your Project</h5>
              </div>
            <div class="card-body">
              <form class="">
                <div class="row">
                  <div class="px-3 col-md-20">
                    <div class="form-group">
                   
                    
                    <select class="form-select form-select-lg pl-1500" aria-label=".form-select-lg example mb-50">
                    <option selected>Open this select menu</option>
                    <option value="1">projectOne</option>
                    <option value="2">projectTwo</option>
                    <option value="3">projectThree</option>
                    </select>
                  </div>
                </div>
              </div>
            <div class="row">
              <div class="update ml-auto mr-auto">
                <button type="submit" class="btn-round btn btn-primary">Select Project</button>
              </div>
            </div>
            </form>
          </div>
       </div>
      </div>
    </div>
  </div>
        
        
      
    </>
  );
}

export default Dashboard;
