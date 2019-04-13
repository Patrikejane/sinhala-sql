import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Dialog from '@material-ui/core/Dialog';
import CircularProgress from '@material-ui/core/CircularProgress';

const styles = {
  paper: {
    backgroundColor: 'transparent',
    boxShadow: 'none',
    overflow: 'hidden',
    color: '#015187',
  },
};

class Loader extends React.Component {
  render() {
    const { classes, open } = this.props;
    return (
      <Dialog
        open={open}
        PaperProps={{
          classes: {
            root: classes.paper,
          },
        }}
      >
        <CircularProgress
          style={{ display: 'inline-block' }}
          size={50}
          thickness={4}
          color={'inherit'}
        />
      </Dialog>
    );
  }
}
Loader.propTypes = {
  classes: PropTypes.object.isRequired,
  open: PropTypes.bool.isRequired,
};
export default withStyles(styles)(Loader);
