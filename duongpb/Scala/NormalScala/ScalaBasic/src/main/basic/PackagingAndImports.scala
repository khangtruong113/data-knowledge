package main.basic

import java.io.Writer

object PackagingAndImports extends  App {

  //poackage members are accesible by their simeple name
  val writer = new Writer() {
    override def write(cbuf: Array[Char], off: Int, len: Int): Unit = ???

    override def flush(): Unit = ???

    override def close(): Unit = ???
  }

  // import the package if you want to access it

  //if you dont want to import, you need to use the full package name instead : for eg: playground.Cinderella = fully qualified name

  //package object
  /**
   * creating a package object -> the name is create automatic
   * 1 package can have only 1 package object file
   * things in package object can be access throughout the whole package
   */

  //imports
//  val prince = new PrinceCharming

  // when we want to change the temp name of the importered object : -> import somewhere.{something1, something2 => changedname}
}
