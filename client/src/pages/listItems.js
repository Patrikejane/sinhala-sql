import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import DashboardIcon from '@material-ui/icons/Dashboard';
import BarChartIcon from '@material-ui/icons/BarChart';

import {Link} from 'react-router-dom';
import PropTypes from 'prop-types';

export const renderLink = itemProps => (
  <Link to={this.props.to} {...itemProps} />
);

class ListItemLink1 extends React.Component {
  renderLink = itemProps => <Link to={this.props.to} {...itemProps} />;

  render () {
    const {icon, primary} = this.props;
    return (
      <li>
        <ListItem button component={this.renderLink}>
          <ListItemIcon>{icon}</ListItemIcon>
          <ListItemText primary={primary} />
        </ListItem>
      </li>
    );
  }
}

ListItemLink1.propTypes = {
  icon: PropTypes.node.isRequired,
  primary: PropTypes.node.isRequired,
  to: PropTypes.string.isRequired,
};

export const mainListItems = (
  <div>
    <ListItemLink1 to="/app/gallery" primary="දත්ත විමසුම" icon={<DashboardIcon />} />
    {/* <ListItemLink1 to="/app/category" primary="Category" icon={<BarChartIcon />} /> */}
  </div>
);
