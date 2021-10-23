module.exports = {
  error(msg = null) {
    return {
      success: false,
      error: msg
    }
  },
  success(data = null) {
    return {
      success: true,
      data
    }
  }
}