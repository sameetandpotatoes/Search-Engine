var React = require('react');
var Search = require('./components/search.react');
var Loader = require('./components/loading.react');
var Index = React.createClass({
  getDefaultProps: function(){
    return {
      'load': false
    };
  },
  getInitialState: function(){
    return {
      'results': [],
      'load': false
    };
  },
  searchSubmitted: function(query){
    console.log(query);
    this.props.load = true;
    this.props.afterSearch = true;
    this.forceUpdate();

    // Call search
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
    } else {
      return (
        <div className="row-fluid">
          Hello World From React.JS
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
