package main.OOP

object Enums {
  enum Permissions {
    case READ, WRITE, EXECUTE, NONE

    def openDocument(): Unit =
      if(this == READ) {
        println("opening document")

      }
      else println("reading not allowed")
  }
// enum is the data type that we can iterate through all element of that types

  val somePermissions: Permissions = Permissions.READ

  enum permissionsWithBits(bits: Int){
    case READ extends permissionsWithBits(4) //100
    case WRITE extends permissionsWithBits(2) // 010
    case EXECUTE extends permissionsWithBits(1) ///001
    case NONE extends permissionsWithBits(0) //000
  }

  //companion object
  object permissionsWithBits {
    def fromBits(bits: Int): permissionsWithBits =
      permissionsWithBits.NONE
  }

  //standard API
  val somePermissionOrdinal = somePermissions.ordinal
  val allPermissions = permissionsWithBits.values //array of all posible permission values
  val readPermission: Permissions = Permissions.valueOf("READ") //Permission.READ
  def main(args: Array[String]): Unit = {
    somePermissions.openDocument()
  }
}
