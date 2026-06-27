import React, { createContext, useContext, useState, useEffect } from 'react';
import { 
  signInWithEmailAndPassword, 
  createUserWithEmailAndPassword, 
  signOut as firebaseSignOut, 
  onAuthStateChanged,
  updateProfile
} from 'firebase/auth';
import { auth } from '../firebase';
import { apiService } from '../api';

const AuthContext = createContext();

export function useAuth() {
  return useContext(AuthContext);
}

export function AuthProvider({ children }) {
  const [currentUser, setCurrentUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [isDemoMode, setIsDemoMode] = useState(false);
  const [theme, setThemeState] = useState('dark');

  const updateTheme = (newTheme) => {
    setThemeState(newTheme);
    if (newTheme === 'light') {
      document.body.classList.add('theme-light');
      document.body.classList.remove('theme-dark');
    } else {
      document.body.classList.add('theme-dark');
      document.body.classList.remove('theme-light');
    }
  };

  // Sign up function
  function signup(email, password, displayName) {
    setIsDemoMode(false);
    return createUserWithEmailAndPassword(auth, email, password)
      .then(async (userCredential) => {
        if (displayName) {
          await updateProfile(userCredential.user, { displayName });
        }
        return userCredential.user;
      });
  }

  // Login function
  function login(email, password) {
    setIsDemoMode(false);
    return signInWithEmailAndPassword(auth, email, password);
  }

  // Enable Demo Mode
  function tryDemoMode() {
    setIsDemoMode(true);
    const mockUser = {
      uid: 'demo_user',
      displayName: 'Demo Hero',
      email: 'demo@ecotrack.org',
      isDemo: true
    };
    setCurrentUser(mockUser);
    setLoading(false);
    return Promise.resolve(mockUser);
  }

  // Logout function
  function logout() {
    if (isDemoMode) {
      setIsDemoMode(false);
      setCurrentUser(null);
      return Promise.resolve();
    }
    return firebaseSignOut(auth);
  }

  // Get current token (demo vs live Firebase token)
  async function getAuthToken() {
    if (isDemoMode) {
      return 'demo_token';
    }
    if (!auth.currentUser) return null;
    return await auth.currentUser.getIdToken(true);
  }

  useEffect(() => {
    // Check if we are running standard Firebase
    const unsubscribe = onAuthStateChanged(auth, (user) => {
      // If we are in demo mode, ignore Firebase auth changes unless logged out
      if (!isDemoMode) {
        setCurrentUser(user);
        setLoading(false);
      }
    });

    return unsubscribe;
  }, [isDemoMode]);

  useEffect(() => {
    async function loadUserTheme() {
      if (currentUser) {
        try {
          const token = await getAuthToken();
          if (token) {
            const res = await apiService.getSettings(token);
            if (res.success && res.settings && res.settings.theme) {
              updateTheme(res.settings.theme);
            } else {
              updateTheme('dark');
            }
          }
        } catch (err) {
          console.error('Failed to load user theme', err);
          updateTheme('dark');
        }
      } else {
        updateTheme('dark');
      }
    }
    loadUserTheme();
  }, [currentUser, isDemoMode]);

  const value = {
    currentUser,
    signup,
    login,
    logout,
    tryDemoMode,
    getAuthToken,
    isDemoMode,
    loading,
    theme,
    updateTheme
  };

  return (
    <AuthContext.Provider value={value}>
      {!loading && children}
    </AuthContext.Provider>
  );
}
