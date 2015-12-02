/*
  Reusable component for searching. A smarter search has been implemented to avoid
  unnecessary ajax requests. Whenever the user types, a timer is set. If the user
  does not press a key within the allotted time, the search will be executed.
  Otherwise, the timer will be reset.

  Inputs
  @prop onChange()
  @prop disabled (true/false): If disabled, then this component won't fire off
  any events. Again, this is implemented so when the parent is loading, the user
  can't fire off more search events and slow down the application
*/

var React = require('react');
module.exports = React.createClass({
  getDefaultProps: function(){
    return{
      'typingTimer': null,
      'delayInterval': 500,
      'search_query': ''
    };
  },
  handleSubmit: function(){
    if (!this.props.disabled){
      if (this.props.typingTimer != null){
        clearTimeout(this.props.typingTimer);
      }
      //Set timeout before executing search
      this.props.typingTimer = setTimeout(this.submitSearch, this.props.delayInterval);
    }
  },
  submitSearch: function(){
    if (!this.props.disabled){
      this.props.search_query = this.refs.input.getDOMNode().value;
      //Calls parent component's onChange, which is passed into the props
      this.props.onChange(this.props.search_query);
    }
  },
  render: function(){
    var placeholder = "Enter an ingredient or name of a recipe to see results!";
    if (this.props.showHeader){
      return (
        <header>
          <a href="#">Food Me Food</a>
          <div className="search">
            <input type="text" placeholder={this.props.value == "" ? placeholder : null} ref="input" onChange={this.handleSubmit} defaultValue={this.props.value != "" ? this.props.value : null} />
            <div className="btn-normal btn-search blue" onClick={this.submitSearch}>Search</div>
          </div>
        </header>
      );
    } else{
      return (
        <div className="search">
          <input type="text" placeholder={this.props.value == "" ? placeholder : null} ref="input" onChange={this.handleSubmit} defaultValue={this.props.value != "" ? this.props.value : null} />
          <div className="btn-normal btn-search blue" onClick={this.submitSearch}>Search</div>
        </div>
      );
    }
  }
});
