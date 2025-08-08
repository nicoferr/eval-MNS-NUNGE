import './App.css'
import { BrowserRouter, Route, Routes, Outlet, NavLink } from 'react-router-dom'
import Form from './components/Form'
import History from './components/History'

function App() {

  return (
    <>
      <BrowserRouter>
        <header className='flex bg-gray-200 rounded'>
          <nav className='flex w-full'>
            <NavLink className="p-2 hover:bg-gray-400 hover:text-white" to="/">Accueil</NavLink>
            <NavLink className="p-2 hover:bg-gray-400 hover:text-white" to="/history" >Historique des cocktails</NavLink>
          </nav>
        </header>
        <Routes>
          <Route path="/" element={<Form />} />
          <Route path="/history" element={<History />} />
        </Routes>
      </BrowserRouter>
      <Outlet></Outlet>
    </>
  )
}

export default App
