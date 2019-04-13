import React from 'react';
import PropTypes from 'prop-types';
import {withStyles} from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import {Chart} from 'react-google-charts';
import CircularProgress from '@material-ui/core/CircularProgress';
import Grid from '@material-ui/core/Grid';
import axios from 'axios';

const baseURL = 'http://localhost:5000';

const styles = {
  root: {
    flexGrow: 1,
  },
  table: {
    minWidth: 700,
  },
  card: {
    padding: '10px 10px 10px 10px',
  },
};

class Category extends React.Component {
  state = {};

  countryBreakDown = () => {
    axios
      .get (`${baseURL}/api/statpie/country/`)
      .then (response => {
        this.setState ({countryBreakDown: response.data});
      })
      .catch (error => console.log (error));
  };

  mostViewedRecipes = () => {
    axios
      .get (`${baseURL}/api/stattable/view/`)
      .then (response => {
        this.setState ({mostViewedRecipes: response.data});
      })
      .catch (error => console.log (error));
  };

  mealTypeBreakDown = () => {
    axios
      .get (`${baseURL}/api/statpie/mealtype/`)
      .then (response => {
        this.setState ({mealTypeBreakDown: response.data});
      })
      .catch (error => console.log (error));
  };

  componentDidMount () {
    this.countryBreakDown ();
    this.mealTypeBreakDown ();
    this.mostViewedRecipes();
  }

  render () {
    const {classes} = this.props;
    const {countryBreakDown, mealTypeBreakDown, mostViewedRecipes} = this.state;
    return (
      <div>
        <Grid container spacing={24} className={classes.root}>
          <Grid item>
            <Paper className={classes.card}>
              <Chart
                width={'500px'}
                height={'300px'}
                chartType="PieChart"
                loader={<CircularProgress className={classes.progress} />}
                data={countryBreakDown}
                options={{
                  title: 'Country wise breakdown',
                }}
                rootProps={{'data-testid': '1'}}
              />
            </Paper>
          </Grid>
          <Grid item>
            <Paper className={classes.card}>
              <Chart
                width={'500px'}
                height={'300px'}
                chartType="PieChart"
                loader={<CircularProgress className={classes.progress} />}
                data={mealTypeBreakDown}
                options={{
                  title: 'Meal wise breakdown',
                }}
                rootProps={{'data-testid': '2'}}
              />
            </Paper>
          </Grid>
          <Grid item>
            <Paper className={classes.card}>
              <Chart
                width={'500px'}
                height={'300px'}
                chartType="Bar"
                loader={<CircularProgress className={classes.progress} />}
                data={mostViewedRecipes}
                options={{
                  chart: {
                    title: 'Most viewed recipes',
                  },
                }}
                rootProps={{'data-testid': '3'}}
              />
            </Paper>
          </Grid>
        </Grid>

      </div>
    );
  }
}

Category.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles (styles) (Category);
