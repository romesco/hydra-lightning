## Unique Aspects of This Repo

We are striving for this repo to be a close to 'self-maintained' as possible.
A decent amount of the core code (the configuration files themselves) are auto-generated
by a tool called `configen` which we are working on directly within `hydra`. Generally,
users of these configs do not have to understand how to use `configen`. However, if you
plan to contribute, it will be much easier if you have taken a look at
[how `configen` works](https://github.com/facebookresearch/hydra/tree/master/tools/configen) first.

Put simply, think of the directory `/configen` as the source for the core configs. To expand this,
we edit `/configen/conf` and then regenerate. Currently, this is done through `generate_configs.py`,
but this may be updated.

## Pull Requests

We're ready for your pull requests! Don't be shy about it. If you are working through
and idea, put it up as soon as you can as a "draft" PR, and we will offer help.

Here's the workflow:

1. Fork the repo and create your feature branch from `main`.
2. If you've added code, add suitable tests.
3. Ensure the test suite and lint pass.

## Issues

Please file issue if you require a new config we have not provided, have an idea for a useful tutorial, or notice a bug.

## License

By contributing to `hydra-lightning`, you agree that your contributions will be licensed
under the LICENSE file in the root directory of this source tree.
