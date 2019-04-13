import React from 'react';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogTitle from '@material-ui/core/DialogTitle';
import ThumbUp from '@material-ui/icons/ThumbUp';
import ThumbDown from '@material-ui/icons/ThumbDown';
import Grid from '@material-ui/core/Grid';

import Typography from '@material-ui/core/Typography';

import DeleteIcon from '@material-ui/icons/Delete';



function ViewRecipeDialog (props) {
  const {data} = props;
  return (
    <div>
      <Dialog
        open={props.open}
        onClose={props.handleClose}
        aria-labelledby="form-dialog-title"
      >
        <DialogTitle id="form-dialog-title">
          {data.recipeName || '-'}
        </DialogTitle>
        <DialogContent>
          <Grid container spacing={24}>
            <Grid item xs={12}>

              <Typography variant="subtitle2">
                Description
              </Typography>

              <Typography variant="subtitle1">
                {data.description}
              </Typography>

            </Grid>
            <Grid item xs={12}>

              <Typography variant="subtitle2">
                Ingredients
              </Typography>
              <Typography variant="subtitle1">
                {data.ingredients}
              </Typography>

              {/* <List dense={true}>
                {data.ingredients && data.ingredients.map (value => (
                  <ListItem>
                    <Typography variant="subtitle1">
                      {value}
                    </Typography>
                  </ListItem>
                ))}
              </List> */}

            </Grid>
            <Grid item xs={12}>

              <Typography variant="subtitle2">
                Instructions
              </Typography>

              <Typography variant="subtitle1">
                {data.instructions}
              </Typography>

            </Grid>
            <Grid item xs={4}>
              <Typography variant="subtitle2">
                Prep Time (Minutes)
              </Typography>
              <Typography variant="subtitle1">
                {data.prepTime}
              </Typography>

            </Grid>
            <Grid item xs={4}>
              <Typography variant="subtitle2">
                Cook Time (HH:MM)
              </Typography>
              <Typography variant="subtitle1">
                {data.cookTime}
              </Typography>
            </Grid>
            <Grid item xs={4}>
              <Typography variant="subtitle2">
                Total Time (HH:MM)
              </Typography>
              <Typography variant="subtitle1">
                {data.totalTime}
              </Typography>
            </Grid>
            <Grid item xs={12}>
              <Typography variant="subtitle2">
                Yield (Servings)
              </Typography>
              <Typography variant="subtitle1">
                {data.yield}
              </Typography>
            </Grid>
            <Grid item xs={6}>
              <Typography variant="subtitle2">
                Calories
              </Typography>
              <Typography variant="subtitle1">
                {data.calories}
              </Typography>

            </Grid>
            <Grid item xs={6}>
              <Typography variant="subtitle2">
                Fat
              </Typography>
              <Typography variant="subtitle1">
                {data.fat}
              </Typography>
            </Grid>
            <Grid item xs={6}>
              <Typography variant="subtitle2">
                Country of origin
              </Typography>
              <Typography variant="subtitle1">
                {data.country}
              </Typography>
            </Grid>
            <Grid item xs={6}>
              <Typography variant="subtitle2">
                Type of meal
              </Typography>
              <Typography variant="subtitle1">
                {data.mealType}
              </Typography>
            </Grid>
            <Grid item xs={6}>
              <Typography variant="subtitle2">
                Image name
              </Typography>
              <Typography variant="subtitle1">
                {data.imageName}
              </Typography>
            </Grid>
          </Grid>

        </DialogContent>
        <DialogActions>
        <Button onClick={() => props.handleDelete(data.id)} color="secondary">
            <DeleteIcon />
          </Button>
          <Button  onClick={() => props.handleRecipeVote("upVotes", data.id)} color="primary">
            <ThumbUp />
          </Button>
          <Button onClick={() => props.handleRecipeVote("downVotes", data.id)} >
            <ThumbDown />
          </Button>

          <Button onClick={props.handleClose} color="primary">
            Close
          </Button>
          <Button onClick={props.handleUpdateClick} color="primary">
            Update
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}

export default ViewRecipeDialog;
