import Dashboard from "views/Dashboard.js";
import Notifications from "views/Notifications.js";
import Icons from "views/Icons.js";
import Typography from "views/Typography.js";
import TableList from "views/Tables.js";
import Maps from "views/Map.js";
import UserPage from "views/User.js";
import UpgradeToPro from "views/Upgrade.js";

// My Pages
import Login from "Login/Login.js";
import Signup from "Signup/Signup.js";
import Project from "Project/Project.js";
import Calendar from "Calendar/Calendar.js";
import ViewProjects from "ViewProjects/ViewProjects.js";

var routes = [
  //My Pages
  {
    path: "/login",
    name: "Login",
    icon: "nc-icon nc-caps-small",
    component: Login,
    layout: "/user",
  },
  {
    path: "/signup",
    name: "Signup",
    icon: "nc-icon nc-caps-small",
    component: Signup,
    layout: "/user",
  },
  {
    path: "/create_project",
    name: "Create Project",
    icon: "nc-icon nc-caps-small",
    component: Project,
    layout: "/user",
  },
  {
    path: "/Calendar",
    name: "Calendar",
    icon: "nc-icon nc-caps-small",
    component: Calendar,
    layout: "/user",
  },
  {
    path: "/ViewProjects",
    name: "ViewProjects",
    icon: "nc-icon nc-caps-small",
    component: ViewProjects,
    layout: "/user",
  },
  //Default
  {
    path: "/dashboard",
    name: "Dashboard",
    icon: "nc-icon nc-bank",
    component: Dashboard,
    layout: "/admin",
  },
  {
    path: "/icons",
    name: "Icons",
    icon: "nc-icon nc-diamond",
    component: Icons,
    layout: "/admin",
  },
  {
    path: "/maps",
    name: "Maps",
    icon: "nc-icon nc-pin-3",
    component: Maps,
    layout: "/admin",
  },
  {
    path: "/notifications",
    name: "Notifications",
    icon: "nc-icon nc-bell-55",
    component: Notifications,
    layout: "/admin",
  },
  {
    path: "/user-page",
    name: "User Profile",
    icon: "nc-icon nc-single-02",
    component: UserPage,
    layout: "/admin",
  },
  {
    path: "/tables",
    name: "Table List",
    icon: "nc-icon nc-tile-56",
    component: TableList,
    layout: "/admin",
  },
  {
    path: "/typography",
    name: "Typography",
    icon: "nc-icon nc-caps-small",
    component: Typography,
    layout: "/admin",
  },
  {
    pro: true,
    path: "/upgrade",
    name: "Upgrade to PRO",
    icon: "nc-icon nc-spaceship",
    component: UpgradeToPro,
    layout: "/admin",
  },
];
export default routes;
