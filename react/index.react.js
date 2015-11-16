var React = require('react');
var Search = require('./components/search.react');
var Loader = require('./components/loading.react');
var $ = require('jquery');
var Index = React.createClass({
  getDefaultProps: function(){
    return {
      'load': false
    };
  },
  getInitialState: function(){
    return {
      'results': []
    };
  },
  searchSubmitted: function(query){
    console.log(query);
    this.props.load = true;
    this.props.afterSearch = true;
    this.forceUpdate();
    console.log('http://localhost:8000/recipes?q='+query);
    // Call search
    $.get('http://localhost:8000/recipes?q='+query, function(recipes){
      this.setState({
        results: recipes
      });
    }.bind(this));
  },
  componentWillUpdate: function(nextProps, nextState){
    this.props.load = false;
    if (this.props.afterSearch){
      this.props.load = true;
      this.props.afterSearch = false;
    }
  },
  render: function() {
    console.log("Load is " + this.props.load);
    var search_title = "Food Me Food!";
    var placeholder = "Enter an ingredient or name of a recipe to see results!";
    if (this.props.load){
      return (
        <div className="row-fluid">
          Loading
          <Search onChange={this.searchSubmitted} search_title={search_title} placeholder={placeholder} disabled={true}/>
        </div>
      );
    } else if (this.state.results.recipes != null && this.state.results.recipes.length > 0){
      return (
        <div className="row-fluid">
          Results
          <Search onChange={this.searchSubmitted} search_title={search_title} placeholder={placeholder} disabled={false}/>
          <ul>
            {this.state.results.recipes.map(function(recipe){
              return(
                <li>
                  <img src={recipe.image_url} width="25" height="25"></img>
                  <p>{recipe.title}</p>
                </li>
              );
            }, this)}
          </ul>
        </div>
      );
    } else {
      return(
        <div className="row-fluid">
          <Search onChange={this.searchSubmitted} search_title={search_title} placeholder={placeholder} disabled={false}/>
        </div>
      );
    }
  }
});

React.render(
  <Index />,
  document.getElementById('main-content')
);
