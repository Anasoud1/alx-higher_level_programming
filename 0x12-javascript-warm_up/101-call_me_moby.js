#!/usr/bin/node
function callMeMoby (n, exe) {
  for (let i = 0; i < n; i++) {
    exe();
  }
}
module.exports = {
  callMeMoby
};
