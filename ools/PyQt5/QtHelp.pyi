# The PEP 484 type hints stub file for the QtHelp module.
#
# Generated by SIP 6.8.6
#
# Copyright (c) 2024 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt5.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing

import PyQt5.sip

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., Any], QtCore.pyqtBoundSignal]

# Convenient aliases for complicated OpenGL types.
PYQT_OPENGL_ARRAY = typing.Union[typing.Sequence[int], typing.Sequence[float],
        PyQt5.sip.Buffer, None]
PYQT_OPENGL_BOUND_ARRAY = typing.Union[typing.Sequence[int],
        typing.Sequence[float], PyQt5.sip.Buffer, int, None]


class QCompressedHelpInfo(PyQt5.sipsimplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QCompressedHelpInfo') -> None: ...

    def isNull(self) -> bool: ...
    @staticmethod
    def fromCompressedHelpFile(documentationFileName: typing.Optional[str]) -> 'QCompressedHelpInfo': ...
    def version(self) -> QtCore.QVersionNumber: ...
    def component(self) -> str: ...
    def namespaceName(self) -> str: ...
    def swap(self, other: 'QCompressedHelpInfo') -> None: ...


class QHelpContentItem(PyQt5.sipsimplewrapper):

    def childPosition(self, child: typing.Optional['QHelpContentItem']) -> int: ...
    def parent(self) -> typing.Optional['QHelpContentItem']: ...
    def row(self) -> int: ...
    def url(self) -> QtCore.QUrl: ...
    def title(self) -> str: ...
    def childCount(self) -> int: ...
    def child(self, row: int) -> typing.Optional['QHelpContentItem']: ...


class QHelpContentModel(QtCore.QAbstractItemModel):

    contentsCreated: typing.ClassVar[QtCore.pyqtSignal]
    contentsCreationStarted: typing.ClassVar[QtCore.pyqtSignal]
    def isCreatingContents(self) -> bool: ...
    def columnCount(self, parent: QtCore.QModelIndex = ...) -> int: ...
    def rowCount(self, parent: QtCore.QModelIndex = ...) -> int: ...
    def parent(self, index: QtCore.QModelIndex) -> QtCore.QModelIndex: ...
    def index(self, row: int, column: int, parent: QtCore.QModelIndex = ...) -> QtCore.QModelIndex: ...
    def data(self, index: QtCore.QModelIndex, role: int) -> typing.Any: ...
    def contentItemAt(self, index: QtCore.QModelIndex) -> typing.Optional[QHelpContentItem]: ...
    def createContents(self, customFilterName: typing.Optional[str]) -> None: ...


class QHelpContentWidget(QtWidgets.QTreeView):

    linkActivated: typing.ClassVar[QtCore.pyqtSignal]
    def indexOf(self, link: QtCore.QUrl) -> QtCore.QModelIndex: ...


class QHelpEngineCore(QtCore.QObject):

    def __init__(self, collectionFile: typing.Optional[str], parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    @typing.overload
    def documentsForKeyword(self, keyword: typing.Optional[str]) -> typing.List['QHelpLink']: ...
    @typing.overload
    def documentsForKeyword(self, keyword: typing.Optional[str], filterName: typing.Optional[str]) -> typing.List['QHelpLink']: ...
    @typing.overload
    def documentsForIdentifier(self, id: typing.Optional[str]) -> typing.List['QHelpLink']: ...
    @typing.overload
    def documentsForIdentifier(self, id: typing.Optional[str], filterName: typing.Optional[str]) -> typing.List['QHelpLink']: ...
    def usesFilterEngine(self) -> bool: ...
    def setUsesFilterEngine(self, uses: bool) -> None: ...
    def filterEngine(self) -> typing.Optional['QHelpFilterEngine']: ...
    readersAboutToBeInvalidated: typing.ClassVar[QtCore.pyqtSignal]
    warning: typing.ClassVar[QtCore.pyqtSignal]
    currentFilterChanged: typing.ClassVar[QtCore.pyqtSignal]
    setupFinished: typing.ClassVar[QtCore.pyqtSignal]
    setupStarted: typing.ClassVar[QtCore.pyqtSignal]
    def setAutoSaveFilter(self, save: bool) -> None: ...
    def autoSaveFilter(self) -> bool: ...
    def error(self) -> str: ...
    @staticmethod
    def metaData(documentationFileName: typing.Optional[str], name: typing.Optional[str]) -> typing.Any: ...
    def setCustomValue(self, key: typing.Optional[str], value: typing.Any) -> bool: ...
    def customValue(self, key: typing.Optional[str], defaultValue: typing.Any = ...) -> typing.Any: ...
    def removeCustomValue(self, key: typing.Optional[str]) -> bool: ...
    def linksForKeyword(self, keyword: typing.Optional[str]) -> typing.Dict[str, QtCore.QUrl]: ...
    def linksForIdentifier(self, id: typing.Optional[str]) -> typing.Dict[str, QtCore.QUrl]: ...
    def fileData(self, url: QtCore.QUrl) -> QtCore.QByteArray: ...
    def findFile(self, url: QtCore.QUrl) -> QtCore.QUrl: ...
    @typing.overload
    def files(self, namespaceName: typing.Optional[str], filterAttributes: typing.Iterable[typing.Optional[str]], extensionFilter: typing.Optional[str] = ...) -> typing.List[QtCore.QUrl]: ...
    @typing.overload
    def files(self, namespaceName: typing.Optional[str], filterName: typing.Optional[str], extensionFilter: typing.Optional[str] = ...) -> typing.List[QtCore.QUrl]: ...
    def filterAttributeSets(self, namespaceName: typing.Optional[str]) -> typing.List[typing.List[str]]: ...
    def registeredDocumentations(self) -> typing.List[str]: ...
    def setCurrentFilter(self, filterName: typing.Optional[str]) -> None: ...
    def currentFilter(self) -> str: ...
    @typing.overload
    def filterAttributes(self) -> typing.List[str]: ...
    @typing.overload
    def filterAttributes(self, filterName: typing.Optional[str]) -> typing.List[str]: ...
    def addCustomFilter(self, filterName: typing.Optional[str], attributes: typing.Iterable[typing.Optional[str]]) -> bool: ...
    def removeCustomFilter(self, filterName: typing.Optional[str]) -> bool: ...
    def customFilters(self) -> typing.List[str]: ...
    def documentationFileName(self, namespaceName: typing.Optional[str]) -> str: ...
    def unregisterDocumentation(self, namespaceName: typing.Optional[str]) -> bool: ...
    def registerDocumentation(self, documentationFileName: typing.Optional[str]) -> bool: ...
    @staticmethod
    def namespaceName(documentationFileName: typing.Optional[str]) -> str: ...
    def copyCollectionFile(self, fileName: typing.Optional[str]) -> bool: ...
    def setCollectionFile(self, fileName: typing.Optional[str]) -> None: ...
    def collectionFile(self) -> str: ...
    def setupData(self) -> bool: ...


class QHelpEngine(QHelpEngineCore):

    def __init__(self, collectionFile: typing.Optional[str], parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def searchEngine(self) -> typing.Optional['QHelpSearchEngine']: ...
    def indexWidget(self) -> typing.Optional['QHelpIndexWidget']: ...
    def contentWidget(self) -> typing.Optional[QHelpContentWidget]: ...
    def indexModel(self) -> typing.Optional['QHelpIndexModel']: ...
    def contentModel(self) -> typing.Optional[QHelpContentModel]: ...


class QHelpFilterData(PyQt5.sipsimplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QHelpFilterData') -> None: ...

    def __ne__(self, other: object): ...
    def versions(self) -> typing.List[QtCore.QVersionNumber]: ...
    def components(self) -> typing.List[str]: ...
    def setVersions(self, versions: typing.Iterable[QtCore.QVersionNumber]) -> None: ...
    def setComponents(self, components: typing.Iterable[typing.Optional[str]]) -> None: ...
    def swap(self, other: 'QHelpFilterData') -> None: ...
    def __eq__(self, other: object): ...


class QHelpFilterEngine(QtCore.QObject):

    @typing.overload
    def indices(self) -> typing.List[str]: ...
    @typing.overload
    def indices(self, filterName: typing.Optional[str]) -> typing.List[str]: ...
    def availableVersions(self) -> typing.List[QtCore.QVersionNumber]: ...
    filterActivated: typing.ClassVar[QtCore.pyqtSignal]
    def namespacesForFilter(self, filterName: typing.Optional[str]) -> typing.List[str]: ...
    def removeFilter(self, filterName: typing.Optional[str]) -> bool: ...
    def setFilterData(self, filterName: typing.Optional[str], filterData: QHelpFilterData) -> bool: ...
    def filterData(self, filterName: typing.Optional[str]) -> QHelpFilterData: ...
    def availableComponents(self) -> typing.List[str]: ...
    def setActiveFilter(self, filterName: typing.Optional[str]) -> bool: ...
    def activeFilter(self) -> str: ...
    def filters(self) -> typing.List[str]: ...
    def namespaceToVersion(self) -> typing.Dict[str, QtCore.QVersionNumber]: ...
    def namespaceToComponent(self) -> typing.Dict[str, str]: ...


class QHelpFilterSettingsWidget(QtWidgets.QWidget):

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...

    def applySettings(self, filterEngine: typing.Optional[QHelpFilterEngine]) -> bool: ...
    def readSettings(self, filterEngine: typing.Optional[QHelpFilterEngine]) -> None: ...
    def setAvailableVersions(self, versions: typing.Iterable[QtCore.QVersionNumber]) -> None: ...
    def setAvailableComponents(self, components: typing.Iterable[typing.Optional[str]]) -> None: ...


class QHelpIndexModel(QtCore.QStringListModel):

    indexCreated: typing.ClassVar[QtCore.pyqtSignal]
    indexCreationStarted: typing.ClassVar[QtCore.pyqtSignal]
    def isCreatingIndex(self) -> bool: ...
    def linksForKeyword(self, keyword: typing.Optional[str]) -> typing.Dict[str, QtCore.QUrl]: ...
    def filter(self, filter: typing.Optional[str], wildcard: typing.Optional[str] = ...) -> QtCore.QModelIndex: ...
    def createIndex(self, customFilterName: typing.Optional[str]) -> None: ...
    def helpEngine(self) -> typing.Optional[QHelpEngineCore]: ...


class QHelpIndexWidget(QtWidgets.QListView):

    documentsActivated: typing.ClassVar[QtCore.pyqtSignal]
    documentActivated: typing.ClassVar[QtCore.pyqtSignal]
    def activateCurrentItem(self) -> None: ...
    def filterIndices(self, filter: typing.Optional[str], wildcard: typing.Optional[str] = ...) -> None: ...
    linksActivated: typing.ClassVar[QtCore.pyqtSignal]
    linkActivated: typing.ClassVar[QtCore.pyqtSignal]


class QHelpLink(PyQt5.sipsimplewrapper):

    title = ... # type: typing.Optional[str]
    url = ... # type: QtCore.QUrl

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QHelpLink') -> None: ...


class QHelpSearchQuery(PyQt5.sipsimplewrapper):

    class FieldName(int):
        DEFAULT = ... # type: QHelpSearchQuery.FieldName
        FUZZY = ... # type: QHelpSearchQuery.FieldName
        WITHOUT = ... # type: QHelpSearchQuery.FieldName
        PHRASE = ... # type: QHelpSearchQuery.FieldName
        ALL = ... # type: QHelpSearchQuery.FieldName
        ATLEAST = ... # type: QHelpSearchQuery.FieldName

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, field: 'QHelpSearchQuery.FieldName', wordList: typing.Iterable[typing.Optional[str]]) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QHelpSearchQuery') -> None: ...


class QHelpSearchEngine(QtCore.QObject):

    def __init__(self, helpEngine: typing.Optional[QHelpEngineCore], parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def searchInput(self) -> str: ...
    def searchResults(self, start: int, end: int) -> typing.List['QHelpSearchResult']: ...
    def searchResultCount(self) -> int: ...
    searchingFinished: typing.ClassVar[QtCore.pyqtSignal]
    searchingStarted: typing.ClassVar[QtCore.pyqtSignal]
    indexingFinished: typing.ClassVar[QtCore.pyqtSignal]
    indexingStarted: typing.ClassVar[QtCore.pyqtSignal]
    def cancelSearching(self) -> None: ...
    @typing.overload
    def search(self, queryList: typing.Iterable[QHelpSearchQuery]) -> None: ...
    @typing.overload
    def search(self, searchInput: typing.Optional[str]) -> None: ...
    def cancelIndexing(self) -> None: ...
    def reindexDocumentation(self) -> None: ...
    def hits(self, start: int, end: int) -> typing.List[typing.Tuple[str, str]]: ...
    def hitCount(self) -> int: ...
    def resultWidget(self) -> typing.Optional['QHelpSearchResultWidget']: ...
    def queryWidget(self) -> typing.Optional['QHelpSearchQueryWidget']: ...
    def query(self) -> typing.List[QHelpSearchQuery]: ...


class QHelpSearchResult(PyQt5.sipsimplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, other: 'QHelpSearchResult') -> None: ...
    @typing.overload
    def __init__(self, url: QtCore.QUrl, title: typing.Optional[str], snippet: typing.Optional[str]) -> None: ...

    def snippet(self) -> str: ...
    def url(self) -> QtCore.QUrl: ...
    def title(self) -> str: ...


class QHelpSearchQueryWidget(QtWidgets.QWidget):

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...

    def setSearchInput(self, searchInput: typing.Optional[str]) -> None: ...
    def searchInput(self) -> str: ...
    def setCompactMode(self, on: bool) -> None: ...
    def isCompactMode(self) -> bool: ...
    search: typing.ClassVar[QtCore.pyqtSignal]
    def collapseExtendedSearch(self) -> None: ...
    def expandExtendedSearch(self) -> None: ...
    def setQuery(self, queryList: typing.Iterable[QHelpSearchQuery]) -> None: ...
    def query(self) -> typing.List[QHelpSearchQuery]: ...


class QHelpSearchResultWidget(QtWidgets.QWidget):

    requestShowLink: typing.ClassVar[QtCore.pyqtSignal]
    def linkAt(self, point: QtCore.QPoint) -> QtCore.QUrl: ...
