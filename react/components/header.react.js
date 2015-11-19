var React = require('react');
module.exports = React.createClass({
  render: function(){
    if (this.props.showHeader){
      return(
        <header>
          <a href="#">Food Me Food</a>
        </header>
      );
    } else {
      return <div></div>;
    }
  }
});
