/*
  Component that shows a spinning loading icon.
*/

var React = require('react');
module.exports = React.createClass({
  render: function(){
    return(
      <div className="load-container">
        <div className="load"></div>
      </div>
    );
  }
});
