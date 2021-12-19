import React, { useState } from 'react';
import {useHistory } from 'react-router-dom';
import axios from 'axios';
// reactstrap components
import {
  Button,
  Card,
  CardHeader,
  CardBody,
  CardFooter,
  CardTitle,
  FormGroup,
  Form,
  Input,
  Row,
  Col,
} from "reactstrap";

function Project() {

  const history = useHistory();
  const [c_project,setC_project] =useState({name:'',description:'',members:'',startDate:'',endDate:'',tags:''});

  const onChangeHandler = (e) =>{
      const itemName = e.target.name;
      const itemValue = e.target.value;
      setC_project({...c_project,[itemName]:itemValue});
  }

  const onSubmitHandler = async (e)=>{
      e.preventDefault();
      await axios.post('http://localhost:8000/api/v1/rest-auth/create_project/',c_project, {
          "Access-Control-Allow-Origin" : "*",
      })
      .then((resp)=>{
           console.log(resp.data)
          if(resp.data.key !== null && resp.data.user !== null){
              localStorage.setItem('token', resp.data);
              history.push('create_project');
          }else{
              alert('Invalid Email Or Password');
          }
      })
      .catch((error)=>console.log(error))
      .then(setC_project({name:'',description:'',members:'',startDate:'',endDate:'',tags:''}))   
  }

  return (
    <>
      <div className="content">
        <Row>
          <Col className="ml-auto mr-auto" md="8">
            <Card className="card-user">
              <CardHeader>
                <CardTitle tag="h5">Create Project</CardTitle>
              </CardHeader>
              <CardBody>
                <Form>
                  <Row>
                    <Col className="px-1" md="12">
                      <FormGroup>
                        <label>Project Name</label>
                        <Input
                          placeholder="Project Name"
                          type="text"
                          id='projectName'
                          name='name'
                          onChange={onChangeHandler} 
                          value={c_project.name}
                          placeholder="Project Name"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-1" md="12">
                      <FormGroup>
                        <label>Project Description</label>
                        <Input
                          placeholder="Project Description"
                          type="textarea"
                          id='projectDes'
                          name='description'
                          onChange={onChangeHandler} 
                          value={c_project.description}
                          placeholder="Project Description"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col md="12">
                      <FormGroup>
                        <label>Members</label>
                        <Input
                          placeholder="Members"
                          type="text"
                          id='projectMem'
                          name='members'
                          onChange={onChangeHandler} 
                          value={c_project.members}
                          placeholder="Members"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col className="pr-1" md="6">
                      <FormGroup>
                        <label>Start Date</label>
                        <Input
                          placeholder="Start Date"
                          type="date"
                          id='starDate'
                          name='startDate'
                          onChange={onChangeHandler} 
                          value={c_project.startDate}
                          placeholder="Start Date"
                        />
                      </FormGroup>
                    </Col>
                    <Col className="px-1" md="6">
                      <FormGroup>
                        <label>End Date</label>
                        <Input
                          placeholder="End Date"
                          type="date"
                          id='endDate'
                          name='endDate'
                          onChange={onChangeHandler} 
                          value={c_project.endDate}
                          placeholder="End Date"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col md="12">
                      <FormGroup>
                        <label>Tags</label>
                        <Input
                          placeholder="Tags"
                          type="textarea"
                          id='tags'
                          name='tags'
                          onChange={onChangeHandler} 
                          value={c_project.tags}
                          placeholder="Tags"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <div className="update ml-auto mr-auto">
                      <Button
                        className="btn-round"
                        color="primary"
                        type="submit"
                        onClick={onSubmitHandler}
                      >
                        Create Project
                      </Button>
                    </div>
                  </Row>
                </Form>
              </CardBody>
            </Card>
          </Col>
        </Row>
      </div>
    </>
  );
}

export default Project;