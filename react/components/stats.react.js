var React = require('react');
module.exports = React.createClass({
  render: function(){
    return(
      <div className="card">
        <p className="stats-header">About {this.props.stats.total} results ({this.props.stats.elapsed} seconds)</p>
        <p className="stats-header">Page {this.props.stats.page}</p>
      </div>
    );
  }
});
