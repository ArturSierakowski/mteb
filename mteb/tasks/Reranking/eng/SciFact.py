from __future__ import annotations

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskReranking import AbsTaskReranking


class SciFact(AbsTaskReranking):
    metadata = TaskMetadata(
        name="SciFact",
        description="Reranking of scientific abstracts based on their relevance to a given scientific claim. The goal is to retrieve abstracts that support or refute the claim, based on expert annotations.",
        reference="https://arxiv.org/abs/2004.14974",
        dataset={
            "path": "allenai/SciFact",
            "revision": "2d3ad05e857e67e1243ee1698597d38277d04e94",
        },
        type="Reranking",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["eng-Latn"],
        main_score="map",
        date=("2020-04-30", "2020-10-03"),
        domains=["Academic", "Non-fiction"],
        task_subtypes=["Scientific Reranking"],
        license="cc-by-4.0",
        annotations_creators="expert-annotated",
        dialect=[],
        sample_creation="found",
        bibtex_citation="""
@misc{wadden2020factfictionverifyingscientific,
      title={Fact or Fiction: Verifying Scientific Claims}, 
      author={David Wadden and Shanchuan Lin and Kyle Lo and Lucy Lu Wang and Madeleine van Zuylen and Arman Cohan and Hannaneh Hajishirzi},
      year={2020},
      eprint={2004.14974},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2004.14974}, 
}
""",
)