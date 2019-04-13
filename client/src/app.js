import React, {Component} from 'react';
import Dashboard from './pages/Dashboard';
import Login from './pages/Login';
import CssBaseline from '@material-ui/core/CssBaseline';
import {BrowserRouter as Router} from 'react-router-dom';
import { Switch, Route } from 'react-router-dom'

export default class App extends Component {
  render () {
    return (
      <div>
        <CssBaseline />
        <Router>
          <Switch>
            <Route path="/login" component={Login} />
            <Route path="/app" component={Dashboard} />
            <Route exact path="/" component={Login} />
          </Switch>
        </Router>
      </div>
    );
  }
}
