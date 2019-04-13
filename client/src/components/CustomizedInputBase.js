import React from 'react';
import PropTypes from 'prop-types';
import {withStyles} from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import InputBase from '@material-ui/core/InputBase';
import Divider from '@material-ui/core/Divider';
import IconButton from '@material-ui/core/IconButton';
import SearchIcon from '@material-ui/icons/Search';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import Button from '@material-ui/core/Button';
import Chip from '@material-ui/core/Chip';

const styles = {
  root: {
    padding: '2px 4px',
    display: 'flex',
    alignItems: 'center',
    width: 500,
    //marginLeft: '40%',
  },
  input: {
    marginLeft: 8,
    flex: 1,
  },
  iconButton: {
    padding: 10,
  },
  divider: {
    width: 1,
    height: 28,
    margin: 4,
  },
  chip: {
    marginLeft: '5px',
  },
};

class SearchBar extends React.Component {
  state = {
    isAdvanceSearch: false,
    basicSearchValue: '',
    anchorEl: null,
    anchorElType: null,
  };

  handleClick = event => {
    this.setState ({anchorEl: event.currentTarget});
  };

  handleClose = () => {
    this.setState ({anchorEl: null, anchorElType: null});
  };
  handleClickType = event => {
    this.setState ({anchorElType: event.currentTarget});
  };

  handleFilter = data => {
    this.props.handleChangeBasicSearch(data)
    this.handleClose ();
  };

  render () {
    const {anchorEl, anchorElType} = this.state;
    const {
      classes,
      handleChangeBasicSearch,
      handleReset,
      countryMap,
      mealTypeMap,
    } = this.props;



    return (
      <Paper className={classes.root} elevation={1}>
        <InputBase
          className={classes.input}
          placeholder="Search Recipes"
          onChange={e => this.setState ({basicSearchValue: e.target.value})}
          value={this.state.basicSearchValue}
        />
        <IconButton
          className={classes.iconButton}
          aria-label="Search"
          onClick={() => handleChangeBasicSearch ({recipeName:this.state.basicSearchValue})}
        >
          <SearchIcon />
        </IconButton>
        <Divider className={classes.divider} />
        <Button
          color="primary"
          className={classes.button}
          onClick={() => {
            this.setState ({basicSearchValue: ''});
            handleReset ();
          }}
        >
          Reset
        </Button>
        <Divider className={classes.divider} />
        <Button
          color="primary"
          className={classes.button}
          aria-owns={anchorEl ? 'country-menu' : undefined}
          aria-haspopup="true"
          onClick={this.handleClick}
        >
          COUNTRY
        </Button>
        <Divider className={classes.divider} />
        <Button
          color="primary"
          className={classes.button}
          aria-owns={anchorEl ? 'type-menu' : undefined}
          aria-haspopup="true"
          onClick={this.handleClickType}
        >
          TYPE
        </Button>

        <Menu
          id="type-menu"
          anchorEl={anchorElType}
          open={Boolean (anchorElType)}
          onClose={this.handleClose}
        >
          {mealTypeMap &&
            mealTypeMap.map ((mealType, index) => (
              <MenuItem
                key={index}
                onClick={() =>
                  this.handleFilter ({mealType: mealType.mealType})}
              >
                {mealType.mealType}
                {' '}
                <Chip
                  className={classes.chip}
                  label={mealType.count}
                  color="primary"
                />
              </MenuItem>
            ))}

        </Menu>
        <Menu
          id="country-menu"
          anchorEl={anchorEl}
          open={Boolean (anchorEl)}
          onClose={this.handleClose}
        >
          {countryMap &&
            countryMap.map ((country, index) => (
              <MenuItem
                key={index}
                onClick={() => this.handleFilter ({country: country.country})}
              >
                {country.country}
                {' '}
                <Chip
                  className={classes.chip}
                  label={country.count}
                  color="primary"
                />
              </MenuItem>
            ))}
        </Menu>

      </Paper>
    );
  }
}

SearchBar.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles (styles) (SearchBar);
