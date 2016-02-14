var React = require('react');
var Search = require('./components/search.react');
var Loader = require('./components/loading.react');
var SearchResult = require('./components/search_result.react');
var Header = require('./components/header.react');
var StatsHeader = require('./components/stats.react');
var $ = require('jquery');

var Index = React.createClass({
  getDefaultProps: function(){
    return {
      'load': false,
      'base_url': '',
      'query': '',
      'page': 1,
      'first': true
    };
  },
  getInitialState: function(){
    return {
      'results': []
    };
  },
  getMeta: function(param){
    var meta_tags = document.getElementsByTagName('meta');
    for (var i = 0; i < meta_tags.length; i++){
      var meta = meta_tags[i];
      if (meta['name'] == param){
        return meta['content'];
      }
    }
    return '';
  },
  searchSubmitted: function(query){
    //If new query, reset back to first page
    if (query != this.props.query){
      this.props.page = 1;
    }
    if (query != ""){
      this.props.query = query;
      var url = this.props.base_url + '/recipes?q='+query+'&page='+this.props.page;
      this.fetch(url);
    }
  },
  fetch: function(url){
    this.props.first = false;
    this.props.load = true;
    this.props.afterSearch = true;
    this.forceUpdate();
    //Call search
    $.get(url, function(recipes){
      this.setState({
        results: recipes
      });
      window.scrollTo(0,0);
    }.bind(this));
  },
  getRecipes: function(e){
    e.preventDefault();
    var newURL = e.currentTarget.href;
    this.props.page = parseInt(newURL.substring(newURL.length - 1));
    this.fetch(newURL);
  },
  componentWillUpdate: function(nextProps, nextState){
    this.props.load = false;
    if (this.props.afterSearch){
      this.props.load = true;
      this.props.afterSearch = false;
    }
  },
  componentDidMount: function(){
    this.props.base_url = this.getMeta('base_url');
  },
  render: function() {
    var header = <Header showHeader={false}/>;
    var search = <Search onChange={this.searchSubmitted} value={this.props.query} disabled={this.props.load} showHeader={true}/>;
    var loader = this.props.load ? <Loader /> : null;
    var results, next, previous;
    if (this.state.results.recipes != null && this.state.results.recipes.length > 0){
      if (this.state.results.next != null){
        next = <a href={this.state.results.next} onClick={this.getRecipes} className="next"><img src="../static/images/next.png" /></a>;
      }
      if (this.state.results.previous != null){
        previous = <a href={this.state.results.previous} onClick={this.getRecipes} className="previous"><img src="../static/images/previous.png"/></a>;
      }
      results=(
        <div>
          <StatsHeader stats={this.state.results.stats} />
          <ul>
            {this.state.results.recipes.map(function(recipe){
              return <SearchResult recipe={recipe} />;
            }, this)}
          </ul>
        </div>
      );
    } else {
      results = (
        <div className="row-fluid">
          <li className="singleRecipe card">
            <span>Welcome to the search engine for recipes!</span>
            <span>
              With ElasticSearch and a 10,000 row limit on Heroku, Food Me
              Food is able to host almost 10,000 recipes and ingredients
              for your eyes to feast on.
            </span>
            <span>
              Search by ingredients or recipe names, and you will see hundreds of
              results, with images and ingredients.
              Click on the recipe names to see the source website for the recipe.
            </span>
            <span>
              ~ Built by <a href="http://sameetsapra.com" className="recipe-link">Sameet Sapra</a> for SIG-IR
            </span>
          </li>
        </div>
      );
    }
    return(
      <div className="row-fluid" ref="parent">
        {header}
        {loader}
        {search}
        {results}
        <div className="pagination">
          {previous}
          {next}
        </div>
      </div>
    );
  }
});

React.render(
  <Index />,
  document.getElementById('main-content')
);
