import sys

import pytest


# pytest 実行時に -v オプションをつけると reason が出力に見えるようになる
class TestPosixCalls:
    @pytest.mark.skipif(
        sys.platform == 'win32',
        reason="windows上では実行しない"
    )
    def test_skip_win32(self):
        """'win32'プラットフォームではセットアップや実行はされない"""

    @pytest.mark.skipif(
        sys.platform == 'darwin',
        reason="macOS上では実行しない"
    )
    def test_skip_mac_os(self):
        """'darwin'プラットフォームではセットアップや実行はされない"""
    
    @pytest.mark.xfail(
        sys.platform == 'darwin',
        reason="macOS上では動かない"
    )
    def test_xfail(self):
        """'darwin'プラットフォームでは失敗しなければならない"""
        pytest.fail()
