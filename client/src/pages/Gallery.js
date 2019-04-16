import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {withStyles} from '@material-ui/core/styles';
import Grid from '@material-ui/core/Grid';
import NotificationBar from '../components/NotificationBar';
import axios from 'axios';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Loader from '../components/Loader';

import ReactTable from 'react-table';
import 'react-table/react-table.css';

axios.defaults.headers.common['contentType'] = 'application/json';
axios.defaults.headers.common['charset'] = 'UTF-8';

// const baseURL = 'https://demo5358003.mockable.io';
const baseURL = 'http://localhost:5000';

const styles = {
  root: {
    width: '100%',
    flexGrow: 1,
    overflowX: 'auto',
  },
  table: {
    minWidth: 700,
  },
  card: {
    minWidth: '100%',
  },
};

class Gallery extends Component {
  state = {
    notification: {},
    loading: false,
    data: {
      mainInput: '',
      generatedQuery: '',
    },
    error: {
      mainInput: false,
    },

    result:[],
    columns:[]
  };

  handleChange = name => event => {
    console.log(this.isDoubleByte(event.target.value))
    this.setState ({data: {...this.state.data, [name]: event.target.value}});
  };

  capitalizeFirstLetter = string => {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

  handleMainInput = data => {
  console.log(data)
    this.setState ({
      loading: true,
      notification: {showMessages: false},
    });

    axios
      // .post (`${baseURL}/generateQueryInvalid`, data)
      .post (`${baseURL}/generateQuery`, data)
      // .post (`${baseURL}/` , data)

      .then (response => {
        if (response.data.status === 'success') {
          this.setState ({
            loading: false,
            data: {...this.state.data, generatedQuery: response.data.query},
            notification: {
              messages: ['උත්පතන නිර්මාණය කරයි'],
              variant: 'success',
              showMessages: true,
            },
            error: {
              mainInput: false,
            },
          });
        } else if (response.data.status === 'invalid') {
          this.setState ({
            loading: false,
            data: {...this.state.data, generatedQuery: ''},
            notification: {
              messages: ['වලංගු නොවන යෙදවුම්!'],
              variant: 'error',
              showMessages: true,
            },
            error: {
              mainInput: true,
            },
            result:[],
            columns:[]
          });
        }
      })
      .catch (error => {
        this.setState ({
          loading: false,
          data: {...this.state.data, generatedQuery: ''},
          notification: {
            messages: ['ජාල දෝෂය නැවත උත්සාහ කරන්න'],
            variant: 'error',
            showMessages: true,
          },
          result:[],
          columns:[]
        });
      });
  };


  handleQueryInput = data => {
  console.log(data)
    this.setState ({
      loading: true,
      notification: {showMessages: false},
    });

    axios
      .post (`${baseURL}/executeQuery`, data)
      // .post (`${baseURL}/` , data)


      .then (response => {
        if (response.data.status === 'success') {
            console.log("----1--->",response.data.result)
          this.setState ({
            loading: false,
            result: response.data.result,
            columns: response.data.columns,
            notification: {
              messages: ['උත්පතන නිර්මාණය කරයි'],
              variant: 'success',
              showMessages: true,
            },
          });
        } else if (response.data.status === 'invalid') {
          this.setState ({
            loading: false,
            data: {...this.state.data, generatedQuery: ''},
            notification: {
              messages: ['වලංගු නොවන යෙදවුම්!'],
              variant: 'error',
              showMessages: true,
            },
            error: {
              mainInput: true,
            },
          });
        }
      })
      .catch (error => {
        this.setState ({
          loading: false,
          data: {...this.state.data, generatedQuery: ''},
          notification: {
            messages: ['ජාල දෝෂය නැවත උත්සාහ කරන්න'],
            variant: 'error',
            showMessages: true,
          },
        });
      });
  };



  isDoubleByte = (str)  => {
    for (var i = 0, n = str.length; i < n; i++) {
        if (str.charCodeAt( i ) > 255) { return true; }
    }
    return false;
}

  handleRest = () => {
    this.setState ({
      notification: {},
      loading: false,
      data: {
        mainInput: '',
        generatedQuery: '',
      },
      error: {
        mainInput: false,
      },
      result:[],
      columns:[]
    });
  };

  componentDidMount () {}

  render () {

    let temp = []
    this.state.columns.forEach(x => {
    temp.push({
                    Header: this.capitalizeFirstLetter(x),
                    accessor: x,
                  })

    })
    const {classes} = this.props;
    return (
      <div>

        <Loader open={this.state.loading} />
        <Grid
          style={{padding: 0, margin: 0}}
          container
          direction="row"
          justify="flex-end"
          alignItems="center"
        />

        <NotificationBar
          variant={this.state.notification.variant}
          messages={this.state.notification.messages}
          showMessages={this.state.notification.showMessages}
        />

        <Card className={classes.card}>
          <CardContent>
            <Grid
              container
              justify="center"
              alignItems="center"
              spacing={24}
              style={{padding: 0}}
            >

              <Grid item xs={6} style={{paddingTop: 0, paddingBottom: 0}}>
                <TextField
                  error={this.state.error.mainInput}
                  id="outlined-full-width"
                  label="ඔබගේ ප්‍රශ්නය මෙතැනින් විමසන්න"
                  //style={{margin: 8}}
                  //placeholder="Placeholder"
                  helperText={
                    this.state.error.mainInput ? 'වලංගු නොවන යෙදවුම්!' : ''
                  }
                  fullWidth
                  margin="normal"
                  variant="outlined"
                  value={this.state.data.mainInput}
                  onChange={this.handleChange ('mainInput')}
                />
              </Grid>
              <Grid item style={{padding: 0}}>
                <Button
                  variant="contained"
                  color="primary"
                  className={classes.button}
                  disabled={this.state.data.mainInput === ''}
                  onClick={() =>
                    this.handleMainInput ({input: this.state.data.mainInput})}
                >
                  විමසන්න
                </Button>
              </Grid>
              <Grid item xs={2} style={{paddingLeft: 10}}>
                <Button
                  variant="contained"
                  color="primary"
                  className={classes.button}
                  disabled={this.state.data.mainInput === ''}
                  onClick={() => this.handleRest ()}
                >
                  යලි සකසන්න
                </Button>
              </Grid>

            </Grid>
            <Grid
              container
              style={{padding: 0}}
              justify="center"
              alignItems="center"
              spacing={24}
            >

              <Grid item xs={6} style={{paddingTop: 0}}>
                <TextField
//                  disabled={true}
                  id="outlined-full-width"
                  label="උත්පාදිත වියුහ විමසුම් භාෂාව මෙහි දක්වා ඇත"
                  //style={{margin: 8}}
                  //placeholder="Placeholder"
                  //helperText="Full width!"
                  fullWidth
                  margin="normal"
                  variant="outlined"
                  //InputLabelProps={{
                  //shrink: true,
                  //}}
                  value={this.state.data.generatedQuery}
                  onChange={this.handleChange ('generatedQuery')}
                />
              </Grid>
              <Grid item style={{padding: 0}}>
                <Button
                  variant="contained"
                  color="primary"
                  className={classes.button}
                  disabled={this.state.data.generatedQuery === ''}
                   onClick={() =>
                    this.handleQueryInput ({query: this.state.data.generatedQuery})}
                >
                  තහවුරුයි
                </Button>

              </Grid>
              <Grid item xs={2} style={{paddingLeft: 10}} />

            </Grid>

            <Grid style={{paddingTop: 10}}>
            {this.state.columns.length !== 0 &&
              <ReactTable
                data={this.state.result}
//                columns={[
//                  {
//                    Header: 'name',
//                    accessor: 'name',
//                  },
//                  {
//                    Header: 'Name',
//                    accessor: 'firstName',
//                  },
//                  {
//                    Header: 'Name',
//                    accessor: 'firstName',
//                  },
//                  {
//                    Header: 'Name',
//                    accessor: 'firstName',
//                  },
//                  {
//                    Header: 'Name',
//                    accessor: 'firstName',
//                  },
//                  {
//                    Header: 'Name',
//                    accessor: 'firstName',
//                  },
//                ]}
                columns = {temp}
                defaultPageSize={8}
                className="-striped -highlight"
              />
              }
            </Grid>
          </CardContent>

        </Card>

      </div>
    );
  }
}

Gallery.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles (styles) (Gallery);
