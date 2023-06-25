/**
 * Write a function to find the longest common prefix string amongst an array of strings.
 *
 * @param {string[]} strs
 * @returns {string}
 */

function longestCommonPrefix(strs) {
  if (strs.length < 1) return ""
  let prefix = strs[0]
  for (let i = 1; i < strs.length; i++) {
    while (strs[i].indexOf(prefix, 0) !== 0){
      prefix = prefix.slice(0, -1)
      if (prefix < 1) return ""
    }
  }
  return prefix
}

const strs = ["flower","flow","flight"]
console.log(longestCommonPrefix(strs))
