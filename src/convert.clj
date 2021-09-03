(defn build-post-meta-map
  [post-meta]
  (->> post-meta
       (filter not-empty)
       (map #(clojure.string/split % #": " 2))
       (filter (fn [[k v]] (and (not= k "Status")
                                (not (clojure.string/starts-with? k "Category")))))
       (map (fn [[k v]] (if (= k "Tags")
                          [k (clojure.string/split v #", ")]
                          [k v])))
       (map (fn [[k v]] (if (= k "Summary")
                          ["description" v]
                          [k v])))
       (map (fn [[k v]] (assoc {} (keyword (clojure.string/lower-case k)) v)))
       (reduce merge)))
(comment
  (->> "Title: Behavior Driven Development on the JVM with ScalaTest
       Date: 2019-04-08
       Category:
       Tags: bdd, scalatest, scala
       Summary: Clean up your horrible, horrible tests with Behavior Driven Development and ScalaTest!
       Status: published"
       clojure.string/split-lines
       build-post-meta-map)
)


(defn convert-post-meta!
  [filepath]
  (let [post-lines (clojure.string/split-lines (slurp filepath))
        post-meta (take-while not-empty post-lines)
        post-content (drop-while not-empty post-lines)
        post-meta-map (build-post-meta-map post-meta)]
    (spit filepath
          (clojure.string/join "\n" (cons (str post-meta-map) post-content)))))
(comment
  (convert-post-meta! "md/posts/setting-up-ssh-public-key-authentication.md")
)


(defn convert-posts!
  [dir]
  (let [files (rest (file-seq (clojure.java.io/file dir)))
        filepaths (map #(.getPath %) files)]
    (doseq [filepath filepaths]
      (convert-post-meta! filepath))))
(comment
  (convert-posts! "md/posts")
  (convert-posts! "md/pages")
)

