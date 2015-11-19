var React = require('react');
var Search = require('./components/search.react');
var Loader = require('./components/loading.react');
var SearchResult = require('./components/search_result.react');
var Header = require('./components/header.react');
var $ = require('jquery');

var Index = React.createClass({
  getDefaultProps: function(){
    return {
      'load': false,
      'base_url': '',
      'query': '',
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
    if (query != ""){
      this.props.first = false;
      this.props.query = query;
      this.props.load = true;
      this.props.afterSearch = true;
      this.forceUpdate();

      var url = this.props.base_url + '/recipes?q='+query;
      //Call search
      $.get(url, function(recipes){
        this.setState({
          results: recipes
        });
      }.bind(this));
    }
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
    var header = <Header showHeader={this.props.first}/>;
    var search = <Search onChange={this.searchSubmitted} value={this.props.query} disabled={this.props.load} showHeader={!this.props.first}/>;
    var loader = this.props.load ? <Loader /> : null;
    var results;

    if (this.state.results.recipes != null && this.state.results.recipes.length > 0){
      results=(
        <ul>
          {this.state.results.recipes.map(function(recipe){
            return <SearchResult recipe={recipe} />;
          }, this)}
        </ul>
      );
    }
    return(
      <div className="row-fluid">
        {header}
        {loader}
        {search}
        {results}
      </div>
    );
  }
});

React.render(
  <Index />,
  document.getElementById('main-content')
);
