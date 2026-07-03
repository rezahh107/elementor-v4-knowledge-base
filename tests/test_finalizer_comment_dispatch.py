from pathlib import Path


WORKFLOW_PATH = Path(__file__).parent.parent / ".github" / "workflows" / "finalize-stage.yml"


def test_comment_dispatch_requires_exact_command_and_trusted_author() -> None:
    workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert "issue_comment:" in workflow
    assert "github.event.comment.body == '/finalize-stage'" in workflow
    assert "github.event.comment.author_association == 'OWNER'" in workflow
    assert "github.event.comment.author_association == 'MEMBER'" in workflow
    assert "github.event.comment.author_association == 'COLLABORATOR'" in workflow


def test_comment_dispatch_checks_same_repo_and_exact_head() -> None:
    workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert '[[ "$head_repo" == "$GITHUB_REPOSITORY" ]]' in workflow
    assert '[[ "$remote" == "$HEAD_SHA" ]]' in workflow
    assert "persist-credentials: false" in workflow
