Title: Behavior Driven Development on the JVM with ScalaTest
Date: 2019-04-08
Category:
Tags: bdd, scalatest, scala
Summary: Clean up your horrible, horrible tests with Behavior Driven Development and ScalaTest!
Status: published

# Help, My Tests Are Horrible!
Do any of these sound familiar?

* You read a short test case name like `verifySerialization` or `happyPath` and have no idea what it does.
* You read a long test case name like `verifyUserDetailsForCurrentEnabledUnlockedWithoutTenantId` and half way through your eyes glaze over, your ears start ringing, and you have even *less* of an idea what *this* does.
* You read the bodies of two cases and aren't convinced they're different.
* It takes a team of three engineers to figure out:
    * What a test is trying to accomplish.
    * Whether it accomplishes that goal.
    * Whether it should continue to exist.
* You've been handed a ticket from a user and can't tell if it's a bug or a feature. You hunt for the relevant tests for days before closing the ticket as "Can't Reproduce".
* Your JVM devs are getting jealous of your JS devs.

If so, this is **extremely bad and you should panic!** But then *relax*, it will be fine, we can fix this.

# BDD to the Rescue!
Back in 2006 Dan North coined the term Behavior Driven Development (BDD) in his article [Introducing BDD](https://dannorth.net/introducing-bdd/). North describes BDD as an evolution of the practice of [Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development) (TDD) in which "test method names should be sentences" which describe the behavior of systems in scenarios. Developers name test suites and methods according to a domain-specific language (DSL) which describes user stories and scenarios. The names and structure of the test suite therefore maps system behavior directly to tests and vice versa.

The BDD process, much like the TDD process, looks like this:

1. Write a test suite which begins with some story information in the format "As a [role]; I want [feature]; So that [benefit]".
2. Until the story is complete:
    1. Write the next most important test case in the scenario format "Given [initial context]; When [an event occurs]; Then [an outcome occurs]".
    2. Run your test case. It should fail.
    3. Write your implementation code.
    4. Run your test case. It should pass.
    5. Repeat.


Adhering to BDD naming and structuring principles goes a long way to remediate the problems plaguing your horrible, horrible test suite. Gone are the short and semantically meaningless test names. Long test names will be in a predictable format imbued with meaning. Questions of what a test is trying to verify and whether it still belongs in the suite are answered right there in the name. If you're looking for a particular feature, just drill into your test suite and scan for the relevant terms. What's more, your test code is now an **excellent** source of documentation for new (or forgetful) developers.

# And its Trusty Sidekick, ScalaTest!
So now that you're 110% sold on BDD forever you'll want a test framework that facilitates this sort of thing. Might I humbly suggest [ScalaTest](http://www.scalatest.org/)? ScalaTest is a powerful, flexible, readable testing framework "designed to increase your team's productivity through simple, clear tests and executable specifications that improve both code and communication." Wow! And it even has **features!** Let's walk through a few of the best.

## Multiple Test Styles
ScalaTest allows you to write your tests in [multiple test styles](http://www.scalatest.org/user_guide/selecting_a_style). [FeatureSpec](http://doc.scalatest.org/3.0.1/#org.scalatest.FeatureSpec) is the most obvious choice for BDD as its vocabulary consists primarily of features and scenarios. It's great for acceptance tests of your user-facing functionality. From the docs:

```scala
package org.scalatest.examples.featurespec

import org.scalatest._

class TVSet {
  private var on: Boolean = false
  def isOn: Boolean = on
  def pressPowerButton() {
    on = !on
  }
}

class TVSetSpec extends FeatureSpec with GivenWhenThen {

  info("As a TV set owner")
  info("I want to be able to turn the TV on and off")
  info("So I can watch TV when I want")
  info("And save energy when I'm not watching TV")

  feature("TV power button") {
    scenario("User presses power button when TV is off") {

      Given("a TV set that is switched off")
      val tv = new TVSet
      assert(!tv.isOn)

      When("the power button is pressed")
      tv.pressPowerButton()

      Then("the TV should switch on")
      assert(tv.isOn)
    }

    scenario("User presses power button when TV is on") {

      Given("a TV set that is switched on")
      val tv = new TVSet
      tv.pressPowerButton()
      assert(tv.isOn)

      When("the power button is pressed")
      tv.pressPowerButton()

      Then("the TV should switch off")
      assert(!tv.isOn)
    }
  }
}
```

For tests of systems which don't face users try out [WordSpec](http://doc.scalatest.org/3.0.1/#org.scalatest.WordSpec). WordSpec still has a pretty proscriptive BDD vocabulary, but it's not focused on user stories. Again, from the docs:

```scala
package org.scalatest.examples.wordspec

import org.scalatest.WordSpec

class SetSpec extends WordSpec {

  "A Set" when {
    "empty" should {
      "have size 0" in {
        assert(Set.empty.size === 0)
      }

      "produce NoSuchElementException when head is invoked" in {
        assertThrows[NoSuchElementException] {
          Set.empty.head
        }
      }
    }
  }
}
```


## Nested Test Suites
As you may have noticed by now, test suites can be nested to your heart's content. You can nest suites to group test code logically, which makes it easier for fresh eyes to understand your specifications and to find any particular code a bit more quickly. One might create nested suites for scenario, behavior, or even by method as shown below.

```scala
import com.github.nscala_time.time.Imports._
import com.lucidmachinery.bitclock._
import com.lucidmachinery.bitclock.BitClock._
import org.scalatest._

class BitClockSpec extends WordSpec with Matchers {
  "bit" when {
    "the given place value is active in the given digit" should {
      "return One" in {
        bit(8, Digit.Nine)  should be (Bit.One)
        bit(4, Digit.Six)   should be (Bit.One)
        bit(2, Digit.Six)   should be (Bit.One)
        bit(1, Digit.Seven) should be (Bit.One)
      }
    }

    "the given place value is not active in the given digit" should {
      "return Zero" in {
        bit(8, Digit.Seven) should be (Bit.Zero)
        bit(4, Digit.Eight) should be (Bit.Zero)
        bit(2, Digit.Nine)  should be (Bit.Zero)
        bit(1, Digit.Four)  should be (Bit.Zero)
      }
    }
  }

  "bitDigit" when {
    "given a Digit" should {
      "return a Tuple of 4 Bits representing that number" in {
        bitDigit(Digit.Zero)  should be ((Bit.Zero, Bit.Zero, Bit.Zero, Bit.Zero))
        bitDigit(Digit.One)   should be ((Bit.Zero, Bit.Zero, Bit.Zero, Bit.One))
        bitDigit(Digit.Two)   should be ((Bit.Zero, Bit.Zero, Bit.One, Bit.Zero))
        bitDigit(Digit.Three) should be ((Bit.Zero, Bit.Zero, Bit.One, Bit.One))
        bitDigit(Digit.Four)  should be ((Bit.Zero, Bit.One, Bit.Zero, Bit.Zero))
        bitDigit(Digit.Five)  should be ((Bit.Zero, Bit.One, Bit.Zero, Bit.One))
        bitDigit(Digit.Six)   should be ((Bit.Zero, Bit.One, Bit.One, Bit.Zero))
        bitDigit(Digit.Seven) should be ((Bit.Zero, Bit.One, Bit.One, Bit.One))
        bitDigit(Digit.Eight) should be ((Bit.One, Bit.Zero, Bit.Zero, Bit.Zero))
        bitDigit(Digit.Nine)  should be ((Bit.One, Bit.Zero, Bit.Zero, Bit.One))
      }
    }
  }

  "bitTime" when {
    "given a LocalTime" should {
      "return 6 BitDigits representing that LocalTime's time in HHmmss format" in {
        bitTime(LocalTime.parse("12:34:56")) should be ((
          (Bit.Zero, Bit.Zero, Bit.Zero, Bit.One),  // 1
          (Bit.Zero, Bit.Zero, Bit.One , Bit.Zero), // 2
          (Bit.Zero, Bit.Zero, Bit.One, Bit.One),   // 3
          (Bit.Zero, Bit.One, Bit.Zero, Bit.Zero),  // 4
          (Bit.Zero, Bit.One, Bit.Zero, Bit.One),   // 5
          (Bit.Zero, Bit.One, Bit.One, Bit.Zero),   // 6
        ))
      }
    }
  }

  "prettyPrint" when {
    "given a BitTime" should {
      "return the BitTime as columns of BitDigits in the order HHmmss." in {
        val prettyStr = """
                            |0 0 0 0 0 0
                            |0 0 0 1 1 1
                            |0 1 1 0 0 1
                            |1 0 1 0 1 0
                            """.stripMargin('|')
        prettyPrint(bitTime(LocalTime.parse("12:34:56"))) should be (prettyStr)
      }
    }
  }
}
```
  
## Mix-In Functionality
ScalaTest comes with a lot of nice opt-in extensions to its DSL in case you're not yet satisfied. For example, extending your suite with [Matchers](http://www.scalatest.org/user_guide/using_matchers) allows you to use a DSL with vocabulary like `myPredicate should be (true)` or `thisDangList should contain (7)` rather than assert functions. You can mix in [before/after](http://doc.scalatest.org/3.0.1/#org.scalatest.BeforeAndAfter), [beforeEach/afterEach](http://doc.scalatest.org/3.0.1/index.html#org.scalatest.BeforeAndAfterEach), and [beforeAll/afterAll](http://doc.scalatest.org/3.0.1/#org.scalatest.BeforeAndAfterAll) functions in order to manage fixtures shared across test cases or suites. You can extend your suite with [syntactic sugar for your favorite mock framework](http://www.scalatest.org/user_guide/testing_with_mock_objects). You can even mix in [parallel test execution](http://doc.scalatest.org/3.0.1/#org.scalatest.ParallelTestExecution)!

# How Can I Get My Very Own ScalaTest?
[Installing ScalaTest](http://www.scalatest.org/install) is fairly straightforward, about like you'd install any other library.

## In a Scala Project
If you're using [SBT](https://www.scala-sbt.org/) to build your Scala project you just need to add the following dependency to `build.sbt`:

```scala
libraryDependencies += "org.scalactic" %% "scalactic" % "3.0.5"
```

If you're building a Scala project with [Maven](https://maven.apache.org/) like a weirdo add this to your `pom.xml`:

```xml
<dependency>
  <groupId>org.scalatest</groupId>
  <artifactId>scalatest_2.12</artifactId>
  <version>3.0.5</version>
  <scope>test</scope>
</dependency>
```

## In Java
If you have a Java project which desperately needs some ScalaTest injected, and you're building that project with Maven, try adding the following two dependencies and three plugins to your `pom.xml`, as per [Scala in a Java Maven Project ](https://dzone.com/articles/scala-in-java-maven-project) by Alexey Zvolinskiy.

```xml
<dependencies>
  <dependency>
    <groupId>org.scala-lang</groupId>
    <artifactId>scala-library</artifactId>
    <version>2.12.8</version>
  </dependency>

  <dependency>
    <groupId>org.scalatest</groupId>
    <artifactId>scalatest_2.12</artifactId>
    <version>3.0.5</version>
    <scope>test</scope>
  </dependency>
</dependencies>

<build>
  <plugins>
    <plugin>
      <groupId>net.alchim31.maven</groupId>
      <artifactId>scala-maven-plugin</artifactId>
      <executions>
        <execution>
          <id>scala-compile-first</id>
          <phase>process-resources</phase>
          <goals>
            <goal>add-source</goal>
            <goal>compile</goal>
          </goals>
        </execution>
        <execution>
          <id>scala-test-compile</id>
          <phase>process-test-resources</phase>
          <goals>
            <goal>testCompile</goal>
          </goals>
        </execution>
      </executions>
    </plugin>

    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-compiler-plugin</artifactId>
      <configuration>
        <source>1.8</source>
        <target>1.8</target>
      </configuration>
      <executions>
        <execution>
        <phase>compile</phase>
        <goals>
          <goal>compile</goal>
        </goals>
        </execution>
      </executions>
    </plugin>

    <plugin>
      <artifactId>maven-assembly-plugin</artifactId>
      <version>2.5.3</version>
      <configuration>
        <descriptorRefs>
          <descriptorRef>jar-with-dependencies</descriptorRef>
        </descriptorRefs>
        <archive>
          <manifest>
            <mainClass>ScalaRunner</mainClass>
          </manifest>
        </archive>
      </configuration>
      <executions>
        <execution>
          <phase>package</phase>
          <goals>
            <goal>single</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

**DONE.**
