import { lazy } from "react";
import { Navigate, type RouteObject } from "react-router-dom";

const CMSPage = lazy(() => import("./pages/CMSPage"));

export const routes: RouteObject[] = [
  { index: true, element: <Navigate to="complaints" replace /> },
  { path: "complaints", element: <CMSPage /> },
];
