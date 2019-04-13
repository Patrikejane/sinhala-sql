import React from 'react';
import PropTypes from 'prop-types';
import {withStyles} from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
// import Thumb_up from '@material-ui/icons/Thumb_up';
import Visibility from '@material-ui/icons/Visibility';
import ThumbUp from '@material-ui/icons/ThumbUp';
import ThumbDown from '@material-ui/icons/ThumbDown';
import Badge from '@material-ui/core/Badge';
import Pic from './1.jpg';

const styles = {
  card: {
    maxWidth: 345,
    minWidth: 345,
    margin: 8,
  },
  media: {
    height: 140,
  },
  actions: {
    display: 'flex',
  },
  badge: {
    top: '0%',
    right: -8,
  },
};

function MediaCard (props) {
  const {classes} = props;

  return (
    <Badge badgeContent={'New'} invisible={!props.isNew} color="secondary">
      <Card className={classes.card}>
        <CardActionArea>
          <CardMedia
            className={classes.media}
            image= {require(`../images/${props.imageName}`)}
            title="Contemplative Reptile"
          />
          <CardContent>
            <Typography gutterBottom variant="h5" component="h2">
              {props.recipeName}
            </Typography>
            <Typography component="p">
              {props.summary}
            </Typography>

          </CardContent>
        </CardActionArea>
        <CardActions className={classes.actions} disableActionSpacing>
          <Badge
            badgeContent={props.matrics.views}
            classes={{badge: classes.badge}}
            color="secondary"
          >
            <Visibility style={{marginLeft: 10}} />
          </Badge>
          <Badge
            badgeContent={props.matrics.upVotes}
            classes={{badge: classes.badge}}
            color="secondary"
          >
            <ThumbUp style={{marginLeft: 20}} />
          </Badge>
          <Badge
            badgeContent={props.matrics.downVotes}
            classes={{badge: classes.badge}}
            color="secondary"
          >
            <ThumbDown style={{marginLeft: 20}} />
          </Badge>

          <Button
            size="small"
            color="primary"
            onClick={props.handleViewRecipeOpen}
            style={{marginLeft: '30%'}}
            variant="outlined"
          >
            View Recipe
          </Button>
          {/* <Button onClick={() => console.log("sds")} color="secondary">
          <Thumb_up />
        </Button> */}

        </CardActions>
      </Card>
    </Badge>
  );
}

MediaCard.propTypes = {
  classes: PropTypes.object.isRequired,
  recipeName: PropTypes.string.isRequired,
  summary: PropTypes.string.isRequired,
};

export default withStyles (styles) (MediaCard);
