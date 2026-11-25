# fastembed stores the 2.2 GB e5 model in /tmp, so it is re-downloaded after every reboot

## What happens

`FastEmbedEmbedder` (`src/ictkb/embedding.py:100`) creates `TextEmbedding(model_name=...)` without `cache_dir`.
fastembed then falls back to `os.path.join(tempfile.gettempdir(), "fastembed_cache")`, i.e. `/tmp/fastembed_cache`
on Linux (fastembed 0.9.1, `fastembed/common/utils.py`, `define_cache_dir`), unless the `FASTEMBED_CACHE_PATH`
environment variable is set.

`/tmp` is cleared at boot on Ubuntu and most distributions (and is a RAM disk on some). Consequences:

- `intfloat/multilingual-e5-large` (about 2.2 GB) is downloaded again after each reboot.
- A local setup that worked offline stops working offline after a reboot, because the first query needs the network.

Setting `FASTEMBED_CACHE_PATH` in `.env` does **not** help: pydantic-settings reads `.env` into `Settings` but does
not export it to `os.environ`, which is where fastembed looks.

## Proposal

Small change in `src/ictkb/embedding.py` and `config.py` (needs the infrastructure owner's approval):

```python
# config.py
fastembed_cache_dir: Path = Path.home() / ".cache" / "fastembed"

# embedding.py, FastEmbedEmbedder.__init__
self._model = TextEmbedding(model_name=model, cache_dir=str(get_settings().fastembed_cache_dir))
```

`TextEmbedding.__init__` accepts `cache_dir` (checked on fastembed 0.9.1). This makes the setting work from `.env`
like every other setting. A docs-only alternative is to tell contributors to
`export FASTEMBED_CACHE_PATH=$HOME/.cache/fastembed` in the README.

Happy to send the PR if approved.
