var React = require('react');
module.exports = React.createClass({
  render: function(){
    var recipe = this.props.recipe;
    return(
      <li className="singleRecipe card">
        <img src={recipe.image_url} width="300" height="200" className="recipe-image"></img>
        <div className="recipe-description">
          <h1><a target="_blank" href={recipe.url} className="recipe-link"><div dangerouslySetInnerHTML={{__html: recipe.title}} /></a></h1>
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
