import React from "react";

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
                        />
                      </FormGroup>
                    </Col>
                    <Col className="px-1" md="6">
                      <FormGroup>
                        <label>End Date</label>
                        <Input
                          placeholder="End Date"
                          type="date"
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
