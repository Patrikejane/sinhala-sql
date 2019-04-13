import React, { Component } from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import CheckCircleIcon from '@material-ui/icons/CheckCircle';
import ErrorIcon from '@material-ui/icons/Error';
import InfoIcon from '@material-ui/icons/Info';
import green from '@material-ui/core/colors/green';
import amber from '@material-ui/core/colors/amber';
import SnackbarContent from '@material-ui/core/SnackbarContent';
import WarningIcon from '@material-ui/icons/Warning';
import { withStyles } from '@material-ui/core/styles';

const variantIcon = {
  success: CheckCircleIcon,
  warning: WarningIcon,
  error: ErrorIcon,
  info: InfoIcon,
};

const styles = theme => ({
  success: {
    paddingTop: 0,
    paddingBottom: 0,
    marginBottom: theme.spacing.unit,
    minWidth: '100%',
    backgroundColor: green[600],
  },
  error: {
    paddingTop: 0,
    paddingBottom: 0,
    marginBottom: theme.spacing.unit,
    minWidth: '100%',
    backgroundColor: theme.palette.error.dark,
  },
  info: {
    paddingTop: 0,
    paddingBottom: 0,
    marginBottom: theme.spacing.unit,
    minWidth: '100%',
    backgroundColor: theme.palette.primary.dark,
  },
  warning: {
    paddingTop: 0,
    paddingBottom: 0,
    marginBottom: theme.spacing.unit,
    minWidth: '100%',
    backgroundColor: amber[700],
  },
  message: {
    display: 'flex',
    alignItems: 'center',
    padding: 0,
  },
  icon: {
    fontSize: 15,
  },
  iconVariant: {
    opacity: 0.9,
    marginRight: theme.spacing.unit,
  },
  root: {
    paddingTop: 0,
    paddingBottom: 0,
    marginBottom: theme.spacing.unit,
    minWidth: '100%',
  },
});

class NotificationBar extends Component {
  render() {
    const { classes, className, messages, variant, showMessages } = this.props;
    const Icon = variantIcon[variant];


    if (!showMessages) {
      return <div id="messageBar" />;
    }

    return (
      <SnackbarContent
        id="messageBar"
        className={classNames(classes[variant], className)}
        elevation={0}
        message={messages.map((msg, index) => (
          <span key={index} className={classes.message}>
            <Icon className={classNames(classes.icon, classes.iconVariant)} />
            {msg}
          </span>
        ))}
      />
    );
  }
}

NotificationBar.propTypes = {
  classes: PropTypes.object.isRequired,
  messages: PropTypes.arrayOf(PropTypes.string),
  variant: PropTypes.oneOf(['success', 'warning', 'error', 'info']),
};

export default withStyles(styles)(NotificationBar)

