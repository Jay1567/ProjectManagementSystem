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

function Signup() {

  const history = useHistory();
  const [signup,setSignup] =useState({
      email:'',password:'',passwordCnf:''
  });

  const onChangeHandler = (e) =>{
      const itemName = e.target.name;
      const itemValue = e.target.value;
      setSignup({...signup,[itemName]:itemValue});
  }

  const onSubmitHandler = async (e)=>{
      e.preventDefault();
      if(signup.password===signup.passwordCnf && signup.password !== '' && signup.passwordCnf !== ''){
        console.log(signup);
        await axios.post('http://localhost:8000/api/v1/rest-auth/registration/',signup, {
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
      .then(setSignup({email:'',password:'',passwordCnf:''}))
      }else{
        alert('Password and Confirm Password does not match'); 
    }  
  }

  return (
    <>
      <div className="content">
        <Row>
        <Col className="ml-auto mr-auto" md="5">
            <Card className="card-user">
              <CardHeader className="text-center">
                <CardTitle tag="h5">Sign Up</CardTitle>
              </CardHeader>
              <CardBody>
                <Form>
                  <Row>
                    <Col className="pr-1" md="12">
                      <FormGroup>
                        <label>Email</label>
                        <Input
                          type='email'
                          id='emailSignupInput'
                          name='email'
                          onChange={onChangeHandler} 
                          value={signup.email}
                          placeholder="User Name"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                    </Row>
                    {/*<Row>
                    <Col className="pr-1" md="12">
                      <FormGroup>
                        <label>User Name</label>
                        <Input
                          placeholder="User Name"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col md="12">
                      <FormGroup>
                        <label>Company Name</label>
                        <Input
                          placeholder="Company Name"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col md="12">
                      <FormGroup>
                        <label>Mobile</label>
                        <Input
                          placeholder="Mobile"
                          type="number"
                        />
                      </FormGroup>
                    </Col>
                    </Row>*/}
                  <Row>
                    <Col md="12">
                      <FormGroup>
                        <label>Password</label>
                        <Input
                          name='password'
                          onChange={onChangeHandler} 
                          value={signup.password}
                          placeholder="Password"
                          type="password"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col md="12">
                      <FormGroup>
                        <label>Confirm Password</label>
                        <Input
                          name='passwordcnf'
                          onChange={onChangeHandler} 
                          value={signup.passwordCnf}
                          placeholder="Confirm Password"
                          type="password"
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
                        Sign Up
                      </Button>
                    </div>
                    <div className="update ml-auto mr-auto">
                      <Button
                        className="btn-round"
                        color="primary"
                        type="submit"
                      >
                        Login
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

export default Signup;
