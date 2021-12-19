import React, { useState } from 'react';
import {useHistory } from 'react-router-dom';
import axios from 'axios';

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

function Login() {

  const history = useHistory();
  const [signin,setSignin] =useState({
      email:'',
      password:'',
  });

  const onChangeHandler = (e) =>{
      const itemName = e.target.name;
      const itemValue = e.target.value;
      setSignin({...signin,[itemName]:itemValue});
  }

  const onSubmitHandler = async (e)=>{
      e.preventDefault();
      await axios.post('http://localhost:8000/api/v1/rest-auth/login/',signin, {
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
      .then(setSignin({email:'',password:''}))   
  }

  return (
    <>
      <div className="content">
        <Row>
          <Col className="ml-auto mr-auto" md="8">
            <Card className="card-user">
              <CardHeader className="text-center">
                <CardTitle tag="h5">Login</CardTitle>
              </CardHeader>
              <CardBody>
                <Form>
                  <Row>
                  <Col md="12">
                      <FormGroup>
                        <label>User Name</label>
                        <Input
                          type='email'
                          id='emailSigninInput'
                          name='email'
                          onChange={onChangeHandler} 
                          value={signin.email}
                          placeholder="User Name"
                          type="text"
                        />
                      </FormGroup>
                    </Col>
                  </Row>
                  <Row>
                    <Col md="12">
                      <FormGroup>
                        <label>Password</label>
                        <Input
                          name='password'
                          id='passwdSigninInput'
                          value={signin.password}
                          onChange={onChangeHandler} 
                          placeholder="Password"
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
                        Login
                      </Button>
                    </div>
                    <div className="update ml-auto mr-auto">
                      <Button
                        className="btn-round"
                        color="primary"
                        type="submit"
                      >
                        SignUp
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

export default Login;
