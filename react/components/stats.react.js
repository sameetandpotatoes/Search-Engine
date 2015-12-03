var React = require('react');
module.exports = React.createClass({
  render: function(){
    return(
      <div className="card">
        <p className="stats-header">About {this.props.stats.total} results ({this.props.stats.elapsed} seconds)</p>
        <p className="stats-header">Showing {this.props.stats.per_page} results on page {this.props.stats.page} of {this.props.stats.num_pages}</p>
      </div>
    );
  }
});
