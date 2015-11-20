var React = require('react');
//this.props.recipe
module.exports = React.createClass({
  render: function(){
    var recipe = this.props.recipe;
    return(
      <li className="singleRecipe">
        <img src={recipe.image_url} width="300" height="200" className="recipe-image"></img>
        <div className="recipe-description">
          <p><div dangerouslySetInnerHTML={{__html: recipe.title}} /></p>
          <ul>
            {recipe.ingredients.map(function(ingredient){
              return <li><div dangerouslySetInnerHTML={{__html: ingredient}}/></li>;
            }, this)}
          </ul>
        </div>
      </li>
    );
  }
});
