import requests 
import pytest

def test_provinsi():
    list_provinsi = requests.get('https://kodepos-2d475.firebaseio.com/list_propinsi.json?print=pretty')
    data_prov = list_provinsi.json()
    assert len(data_prov) == 34
    assert data_prov.get('p9') == 'Jawa Barat'
    
@pytest.mark.xfail
def test_kotakab_jabar():
    list_kotakab = requests.get('https://kodepos-2d475.firebaseio.com/list_kotakab/p9.json?print=pretty')
    data_kotakab = list_kotakab.json()
    assert list_kotakab.status_code == 200
    assert data_kotakab.get('k60') == 'Tasikmalaya_typo'
    assert len(data_kotakab) == 21
    
def test_kodepos_tasik():
    list_keckel = requests.get('https://kodepos-2d475.firebaseio.com/kota_kab/k60.json?print=pretty')
    data_kodepos = list_keckel.json()
    assert list_keckel.status_code == 200
    assert len(data_kodepos) == 420