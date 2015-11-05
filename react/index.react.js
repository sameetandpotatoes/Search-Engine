var React = require('react');
var Index = React.createClass({
  render: function() {
  	return (
      <div className="row-fluid">
        Hello World
      </div>
  	);
  }
});

React.render(
  <Index />,
  document.getElementById('main-content')
);
