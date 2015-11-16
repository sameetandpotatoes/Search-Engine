var React = require('react');
var Search = require('./components/search.react');
var Loader = require('./components/loading.react');
var $ = require('jquery');
var Index = React.createClass({
  getDefaultProps: function(){
    return {
      'load': false,
      'base_url': ''
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
    this.props.load = true;
    this.props.afterSearch = true;
    this.forceUpdate();

    var url = this.props.base_url + '/recipes?q='+query;
    // Call search
    $.get(url, function(recipes){
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
  componentDidMount: function(){
    this.props.base_url = this.getMeta('base_url');
  },
  render: function() {
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
          First time
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
