const fs = require("fs");
const input = fs.readFileSync('test.txt').toString().trim().split('\n');

const N = Number(input[0])
const list = input.slice(1, N + 1).map((v) => v.split(' ').map(Number))
const M = Number(input[N + 1])
const command = input.slice(N + 2).map((v) => v.trim().split(' '))

// 1 <= 난이도, 알고리즘 분류 <= 100

class Tree {
  constructor(key) {
    this.key = key;
    this.left = null;
    this.right = null;
  }
}

class TreeHash {
  constructor(key, value = null) {
    this.key = key;
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class TreeSet {
  constructor() {
    this.root = null;
  }

  set(key){
    const insertNode = (node, key) => {
      if (!node) return new Tree(key)
      if (key < node.key) node.left = insertNode(node.left, key)
      else if (key > node.key) node.right = insertNode(node.right, key)

      return node;
    }

    this.root = insertNode(this.root, key)
    return this;
  }

  findMin(node){
    while (node.left) node = node.left
    return node
  }

  min(node = this.root) {
    if (!node) return null
    while (node.left) {
      node = node.left
    }
    return node.key
  }

  max(node = this.root){
    if (!node) return null
    while (node.right) {
      node = node.right
    }
    return node.key
  }

  delete(key){
    const deleteNode = (node, key) =>{
      if (!node) return null
      if (key < node.key) node.left = deleteNode(node.left, key)
      else if (key > node.key) node.right = deleteNode(node.right, key)
      else {
        if (!node.left && !node.right) return null;

        if (!node.left) return node.right
        if (!node.right) return node.left

        let minNode = this.findMin(node.right)
        node.key = minNode.key
        node.right = deleteNode(node.right, minNode.key)
      }
      return node;
    }

    this.root = deleteNode(this.root, key);
  }

  inorder(node = this.root, result = []) {
    if (node){
      this.inorder(node.left, result);
      result.push(node.key)
      this.inorder(node.right, result)
    }

    return result
  }
}

class TreeMap {
  constructor() {
    this.root = null;
  }

  set(key, value) {
    const insertNode = (node, key, value) => {
      if (!node) return new TreeHash(key, value);
      if (key < node.key) node.left = insertNode(node.left, key, value)
      else if (key > node.key) node.right = insertNode(node.right, key, value)
      return node;
    }

    this.root = insertNode(this.root, key, value)
  }

  get(key) {
    let node = this.root
    while (node) {
      if (key === node.key) return node.value
      node = key < node.key ? node.left : node.right
    }

    return undefined
  }

  delete(key) {
    const deleteNode = (node, key) => {
      if (!node) return null

      if (key < node.key) node.left = deleteNode(node.left, key);
      else if (key > node.key) node.right = deleteNode(node.right, key)
      else {
        if (!node.left && !node.right) return null;

        if (!node.left) return node.right
        if (!node.right) return node.left

        let minNode = this.findMin(node.right);
        node.key = minNode.key;
        node.value = minNode.value;
        node.right = deleteNode(node.right, minNode.key)
      }

      return node;
    }

    this.root = deleteNode(this.root, key)
  }

  findMin(node) {
    while (node.left) node = node.left
    return node;
  }

  min(node = this.root) { if (!node) return null; while (node.left) node = node.left; return node.key; }
  max(node = this.root) { if (!node) return null; while (node.right) node = node.right; return node.key; }

  find(x, key){
    let node = this.root
    let cand = -1
    while (node) {
      if (x === 1) { 
        if (node.key >= key) {
          cand = node.key;
          node = node.left;
        } else {
          node = node.right;
        }
      } else {
        if (node.key < key) {
          cand = node.key;
          node = node.right;
        } else {
          node = node.left;
        }
      }
    }
    return cand;
  }

  inorder(node = this.root, result = []){
    if (node) {
      this.inorder(node.left, result);
      result.push([node.key, node.value])
      this.inorder(node.right, result);
    }

    return result;
  }
}

const totalTree = new TreeMap();
const groups = {};
const problemClass = {};

const add = (p, c, al) => {
  problemClass[p] = [al, c]

  if (!totalTree.get(c)) {
    totalTree.set(c, new TreeSet().set(p))    
  } else {
    totalTree.get(c).set(p)
  }

  if (!groups[al]) {
    groups[al] = new TreeMap();
    groups[al].set(c, new TreeSet().set(p))
  } else {
    if (!groups[al].get(c)){
      groups[al].set(c, new TreeSet().set(p))
    } else {
      groups[al].get(c).set(p)
    }
  }
}

const recommend = (num, x, al, c) => {
  if (num === 1) {
    if (x === 1) {
      const v = groups[al].max()
      return groups[al].get(v).max()
    } else {
      const v = groups[al].min()
      return groups[al].get(v).min()
    }
  } else if (num === 2) {
    if (x === 1) {
      const v = totalTree.max();
      return totalTree.get(v).max()
    } else {
      const v = totalTree.min();
      return totalTree.get(v).min()
    }
  } else {
    const v = totalTree.find(x, c)
    if (v === -1) return -1
    return x === 1 ? totalTree.get(v).min()
              : totalTree.get(v).max();
  }
}

const solve = (p) => {
  const [al, c] = problemClass[p]
  delete problemClass[p]

  totalTree.get(c).delete(p)
  groups[al].get(c).delete(p)

  if (totalTree.get(c).min() === null) totalTree.delete(c);
  if (groups[al].get(c).min() === null) groups[al].delete(c);
}

list.forEach((v) => {
  const [p, c, al] = v
  add(p, c, al)
})

const ans = [];

command.forEach((v) => {
  if (v[0] === 'add') add(Number(v[1]), Number(v[2]), Number(v[3]))
  else if (v[0] === 'recommend') ans.push(recommend(1, Number(v[2]), Number(v[1]), 0))
  else if (v[0] === 'recommend2') ans.push(recommend(2, Number(v[1]), 0, 0))
  else if (v[0] === 'recommend3') ans.push(recommend(3, Number(v[1]), 0, Number(v[2])))
  else solve(Number(v[1]))
})

console.log(ans.join('\n'))