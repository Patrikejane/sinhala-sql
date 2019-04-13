import React from 'react';
import PropTypes from 'prop-types';
import {withStyles} from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import Typography from '@material-ui/core/Typography';
import {Redirect} from 'react-router-dom';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import CircularProgress from '@material-ui/core/CircularProgress';

import Logo from './CR-Logo-BW.jpg';

const styles = theme => ({
  loginLogo: {
    margin: 'auto',
    display: 'block',
    height: 200,
  },
  infoText: {
    paddingTop: `0.75%`,
  },
  loginButtonContainer: {
    alignItems: 'center',
    textAlign: 'center',
    paddingTop: `1%`,
  },
  loginButton: {
    paddingLeft: theme.spacing.unit * 3,
    paddingRight: theme.spacing.unit * 3,
  },
  content: {
    paddingTop: `5%`,
  },
});

class Dashboard extends React.Component {
  state = {
    loading: false,
    isValidSession: false,
    username: '',
    usernameError: false,
  };



  login = () => {
    const {username} = this.state;

    sessionStorage.setItem ('username', username);
    this.setState ({isValidSession: true});
  };

  handleClickLogin = () => {
    const {username} = this.state;

    if (!username) {
      this.setState ({usernameError: true});
    } else {
      this.setState ({usernameError: false});
      this.changeLoadingState ();
      setTimeout (this.login, 500);
    }
  };

  handleChange = event => {
    this.setState ({username: event.target.value});
  };

  changeLoadingState () {
    this.setState (state => ({
      loading: !state.loading,
    }));
  }

  render () {
    // css classes
    const {classes} = this.props;
    // states
    const {loading} = this.state;
    // props
    const {isValidSession} = this.state;

    if (isValidSession) {
      return <Redirect to={'/app'} />;
    }

    return (
      <Grid
        container
        direction="row"
        justify="center"
        alignItems="center"
        className={classes.content}
      >
        <Grid item xs={12}>
          <img className={classes.loginLogo} alt="logo" src={Logo} />
        </Grid>
        <Grid item className={classes.infoText} xs={12}>
          <Typography
            color="textSecondary"
            align="center"
            variant="subtitle1"
            gutterBottom
          >
            දත්ත සමුදාය සදහා සිංහල භෂා අතුරුමුහුණ
            <br />
          </Typography>

        </Grid>
        <Grid item xs={3}>
          <TextField
            error={this.state.usernameError}
            margin="dense"
            variant="outlined"
            id="name"
            label="පරිශීලක නාමය"
            type="text"
            value={this.state.username}
            onChange={this.handleChange}
            fullWidth
            placeholder="පරිශීලක නාමය"
          />
        </Grid>

        <Grid item xs={12} className={classes.loginButtonContainer}>
          {!loading
            ? <Button
                variant="contained"
                color="primary"
                className={classes.loginButton}
                onClick={this.handleClickLogin}
                id="loginButton"
              >
                ඇතුල් වන්න
              </Button>
            : <CircularProgress />}
        </Grid>
      </Grid>
    );
  }
}

Dashboard.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles (styles) (Dashboard);
