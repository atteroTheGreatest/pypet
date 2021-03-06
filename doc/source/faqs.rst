======================
FAQs and Known Issues
======================

**Q:** My program does not terminate
(i.e. it does not crash but runs forever)
when I use *pypet* in multiprocessing mode
in combination with *matplotlib* and *savefig*!?

    **A:** *Matplotlib* uses *numpy* for linear algebra operations,
    these operations are often necessary when plotting.
    So, to solve the issues take a look at the next question.


**Q:** My program does not terminate
(i.e. it does not crash but runs forever)
when I use *pypet* in multiprocessing mode
in combination with *numpy* and *linalg.inv*
or some similar function!?

    **A:** Numpy uses openBLAS (http://www.openblas.net/) to
    solve linear algebra operations. Yet, there are many
    issues with openBLAS and multiprocessing. To resolve this set the
    environment variable `OPENBLAS_NUM_THREADS=1`.


**Q:**  GitPython does not work. If I specify my repository ``git_repository='./myrepo'``,
pypet crashes with an `AttributeError: 'Repo' object has no attribute 'index'`.
What should I do?

    **A:** You probably have an older version of GitPython (likely 0.1.7), install a newer one.
    If ``pip install GitPython`` still downloads the old version, try ``pip install --pre GitPython``
    or if you simply want to upgrade use ``pip install --upgrade --pre GitPython``.


**Q:**  If I create and environment in an *IPython* console everything becomes gibberish!?

    **A:** Pypet will redirect STDOUT and STDERROR to files. Unfortunately, this messes with
    the *IPython* console. To avoid this simply disable logging of these two streams setting the
    `log_stdout` to `False`: ``env = Environment( ..., log_stdout=False, ...)``.

**Q:** Why can I no longer decide on the search strategy and what happened to `v_check_uniqueness`?

    **A:** Both of them have been removed because they lead to inconsistencies.
    The child nodes of a particular group are not ordered, so tree traversal happens
    arbitrary. Thus, if you search for two nodes with the same name and same depth in the tree,
    the search result also becomes arbitrary. Thus, *pypet* will now always check if
    your search yields a unique result up to a particular depth. Accordingly, `v_check_uniqueness`
    is rendered obsolete. Likewise is depth first search because this automatic checking
    only works with breadth first tree traversal.
    Sorry for any inconvenience caused by this API change.