package data_structures

case class TreeNode(var data: Any, var parent: TreeNode, var left: TreeNode,
    var right: TreeNode) extends Node {

  def this(data: Any) = this(data, null, null, null)
  def this(data: Any, parent: TreeNode) = this(data, parent, null, null)

  override def get(): Any = data
  override def set(newData: Any): Unit = {data = newData}
  override def toString(): String = data.toString()

  def setParent(newParent: TreeNode): Unit = {parent = newParent}
  def setLeft(newLeft: TreeNode): Unit = {
    left = newLeft
    newLeft.setParent(this)
  }
  def setRight(newRight: TreeNode): Unit = {
    right = newRight
    newRight.setParent(this)
  }

  def getParent(): Option[TreeNode] = Option(parent)
  def getLeft(): Option[TreeNode] = Option(left)
  def getRight(): Option[TreeNode] = Option(right)
}

class BinaryTree(private var root: TreeNode) {

  def getRoot(): TreeNode = root
  def setRoot(newRoot: TreeNode): Unit = {root = newRoot}

  def preorder(r: TreeNode = root): String = {
    var toReturn: String = r.toString()
    val left: Option[TreeNode] = r.getLeft()
    val right: Option[TreeNode] = r.getRight()
    if (left.isDefined) {
      toReturn += ", " + preorder(left.get)
    }
    if (right.isDefined) {
      toReturn += ", " + preorder(right.get)
    }
    toReturn
  }

  def inorder(r: TreeNode = root): String = {
    var toReturn:String = ""
    val left: Option[TreeNode] = r.getLeft()
    val right: Option[TreeNode] = r.getRight()
    if (left.isDefined) {
      toReturn += inorder(left.get) + ", "
    }
    toReturn += r.toString()
    if (right.isDefined) {
      toReturn += ", " + inorder(right.get)
    }
    toReturn
  }

  def postorder(r: TreeNode = root): String = {
    var toReturn:String = ""
    val left: Option[TreeNode] = r.getLeft()
    val right: Option[TreeNode] = r.getRight()
    if (left.isDefined) {
      toReturn += postorder(left.get)
    }
    if (right.isDefined) {
      toReturn += ", " + postorder(right.get) + ", "
    }
    toReturn += r.toString()
    toReturn
  }

  override def toString(): String = inorder()
}
