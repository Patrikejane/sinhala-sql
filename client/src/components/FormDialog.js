import React from 'react';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogTitle from '@material-ui/core/DialogTitle';
import MenuItem from '@material-ui/core/MenuItem';
import Grid from '@material-ui/core/Grid';

import {mealType, countries} from './constant'

function FormDialog (props) {

  return (
    <div>
      <Dialog
        open={props.open}
        onClose={props.handleClose}
        aria-labelledby="form-dialog-title"
      >
        <DialogTitle id="form-dialog-title">Add New Recipe</DialogTitle>
        <DialogContent>
          <Grid container spacing={24}>
            <Grid item xs={12}>
              <TextField
                error={props.error.recipeName}
                autoFocus
                margin="dense"
                variant="outlined"
                id="name"
                label="Recipe Name"
                type="text"
                fullWidth
                value={props.data.recipeName}
                onChange={props.handleChange ('recipeName')}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                error={props.error.description}
                margin="dense"
                id="name"
                variant="outlined"
                label="Description"
                type="text"
                fullWidth
                value={props.data.description}
                onChange={props.handleChange ('description')}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                error={props.error.ingredients}
                margin="dense"
                variant="outlined"
                id="name"
                label="Ingredients (comma separated)"
                type="text"
                fullWidth
                value={props.data.ingredients}
                onChange={props.handleChange ('ingredients')}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                error={props.error.instructions}
                multiline
                rowsMax="4"
                margin="dense"
                variant="outlined"
                id="name"
                label="Instructions"
                type="text"
                fullWidth
                value={props.data.instructions}
                onChange={props.handleChange ('instructions')}
              />
            </Grid>
            <Grid item xs={4}>
              <TextField
                error={props.error.prepTime}
                margin="dense"
                variant="outlined"
                id="name"
                label="Prep Time (Minutes)"
                type="text"
                value={props.data.prepTime}
                onChange={props.handleChange ('prepTime')}
                fullWidth
              />
            </Grid>
            <Grid item xs={4}>
              <TextField
                error={props.error.cookTime}
                margin="dense"
                variant="outlined"
                id="name"
                label="Cook Time (HH:MM)"
                type="text"
                value={props.data.cookTime}
                onChange={props.handleChange ('cookTime')}
                fullWidth
              />
            </Grid>
            <Grid item xs={4}>
              <TextField
                error={props.error.totalTime}
                margin="dense"
                variant="outlined"
                id="name"
                label="Total Time (HH:MM)"
                type="text"
                value={props.data.totalTime}
                onChange={props.handleChange ('totalTime')}
                fullWidth
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                error={props.error.yield}
                margin="dense"
                variant="outlined"
                id="name"
                label="Yield (Servings)"
                type="text"
                fullWidth
                value={props.data.yield}
                onChange={props.handleChange ('yield')}
              />
            </Grid>
            <Grid item xs={6}>
              <TextField
                error={props.error.calories}
                margin="dense"
                variant="outlined"
                id="name"
                label="Calories"
                type="text"
                fullWidth
                value={props.data.calories}
                onChange={props.handleChange ('calories')}
              />
            </Grid>
            <Grid item xs={6}>
              <TextField
                error={props.error.fat}
                margin="dense"
                variant="outlined"
                id="name"
                label="Fat"
                type="text"
                fullWidth
                value={props.data.fat}
                onChange={props.handleChange ('fat')}
              />
            </Grid>
            <Grid item xs={6}>

              <TextField
                error={props.error.country}
                select
                margin="dense"
                variant="outlined"
                id="country"
                label="country of origin"
       
                fullWidth
                value={props.data.country}
                onChange={props.handleChange ('country')}
              >
                {countries.map (option => (
                  <MenuItem key={option.value} value={option.value}>
                    {option.value}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>
            <Grid item xs={6}>
              <TextField
                error={props.error.mealType}
                select
                margin="dense"
                variant="outlined"
                id="mealType"
                label="Type of meal"
       
                fullWidth
                value={props.data.mealType}
                onChange={props.handleChange ('mealType')}
              >
                {mealType.map (option => (
                  <MenuItem key={option.value} value={option.value}>
                    {option.label}
                  </MenuItem>
                ))}
              </TextField>

            </Grid>
            <Grid item xs={12}>
              <TextField
                error={props.error.imageName}
                margin="dense"
                variant="outlined"
                id="imageName"
                label="Image Name"
                type="text"
                fullWidth
                value={props.data.imageName}
                onChange={props.handleChange ('imageName')}
              />
            </Grid>
          </Grid>

        </DialogContent>
        <DialogActions>
          <Button onClick={props.handleClose} color="primary">
            Close
          </Button>
          {props.data.id
            ? <Button onClick={props.handleUpdate} color="primary">
                Update
              </Button>
            : <Button onClick={props.handleSave} color="primary">
                Save
              </Button>}

        </DialogActions>
      </Dialog>
    </div>
  );
}

export default FormDialog;
