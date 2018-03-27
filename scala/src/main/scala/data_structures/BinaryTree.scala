package data_structures

case class TreeNode(var data: Any, var parent: TreeNode, var left: TreeNode,
    var right: TreeNode) extends Node {

  def this(data: Any) = this(data, null, null, null)
  def this(data: Any, parent: TreeNode) = this(data, parent, null, null)

  override def get(): Any = data
  override def set(newData: Any): Unit = {data = newData}
  override def toString(): String = data.toString()

  def setParent(newParent: TreeNode): Unit = {parent = newParent}
  def setLeft(newLeft: TreeNode): Unit = {left = newLeft}
  def setRight(newRight: TreeNode): Unit = {right = newRight}

  def getParent(): TreeNode = parent
  def getLeft(): TreeNode = left
  def getRight(): TreeNode = right
}

class BinaryTree(private var root: TreeNode) {

  def getRoot(): TreeNode = root
  def setRoot(newRoot: TreeNode): Unit = {root = newRoot}
}
