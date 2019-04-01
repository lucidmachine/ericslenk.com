Title: Behavior Driven Development on the JVM with ScalaTest
Date: 2019-04-08
Category:
Tags: bdd, jvm, scalatest, scala
Summary:
Status: draft

# Help, My Tests Are Horrible!
* You don't have tests (duh).
* Your test case names look like:
  * verifyLocks - Little semantic meaning
  * [pick a really long nasty JUnit test name].
* Your tests are hard to tell apart.
* Given a behavior of your app OR a line of implementation code, you can't find the relevant test case(s)
  * Note: in mature projects, your test code will be *read* more often than it will be *written*.
* It takes a team of engineers to figure out:
  * What a test is trying to accomplish.
  * How it works.
  * Why it exists at all.
* Your JVM devs are getting jealous of your JS devs.

# BDD to the Rescue!

# Here Comes ScalaTest!
* ScalaTest is a powerful, flexible, readable testing framework
* "ScalaTest is designed to increase your team's productivity through simple, clear tests and executable specifications that improve both code and communication"
 
# Wait, How Does That Help?
* You can pick the test style best suited to your team's needs
  * FunSpec - 
  * WordSpec - 
  * FeatureSpec - 
* Test cases have human-readable names
* Test suites can be arbitrarily nested
  * by impl detail e.g. method
  * by scenario
  * by behavior
* Traits can be used to mix in
  * Matchers - write "should be" instead of an assert expression
  * beforeEach/afterEach methods
  * Parallel test execution
  * syntactic sugar for mocking frameworks e.g. ScalaMock, Mockito

# How Can I Get Started?
* In Scala?
* In Java?
